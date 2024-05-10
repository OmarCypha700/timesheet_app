from django.shortcuts import render, redirect
from .models import Report
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponse
import csv, datetime
# from django.views import View

User = get_user_model()
# Create your views here.
@login_required(login_url='/authentication/login')
def index(request):
    return render(request, 'timesheet_app/index.html')

def timesheet(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        project = request.POST['project']
        duration = request.POST['duration']
        overtime = request.POST['overtime']
        description = request.POST['description']

        Report.objects.create(owner=request.user, name=name, date=date,project=project,duration=duration,overtime=overtime,description=description)
        return redirect('timesheet')
    else:
        reports = Report.objects.filter(owner=request.user)
        context = {
            'reports': reports
        }
        return render(request, 'timesheet_app/timesheet.html', context)


def report(request):
    if request.method == 'POST':
        post_data = request.POST.dict()

        if 'username' in post_data:
            # username = request.POST['username']
            username = post_data.get('username')
            users = User.objects.exclude(username__in =['admin'])
            if username == 'all':
                reports = Report.objects.all()
                context = {
                'reports': reports,
                'users': users,
                }
                return render(request, 'timesheet_app/report.html', context)
            else:
                user = User.objects.get(username__iexact=username)
                user_id = user.id
                reports = Report.objects.filter(owner=user_id)
            context = {
            'reports': reports,
            'users': users,
            'username': username,
            'user_id': user_id
            }
            return render(request, 'timesheet_app/report.html', context)
        else:
            name = post_data.get('name')
            user_id = post_data.get('user_id')
            from_date = post_data.get('from')
            to_date = post_data.get('to')
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename={name}_timesheet_report'+str(datetime.datetime.now())+'.csv'
            if name == 'all':
                reports = Report.objects.filter(date__range=[from_date, to_date])
            else:
                reports = Report.objects.filter(owner=user_id, date__range=[from_date, to_date])
            writer=csv.writer(response)
            writer.writerow(['Name', 'Date', 'Project', 'Description', 'Duration (minutes)', 'Overtime (minutes)'])
            for report in reports:
                writer.writerow([report.name, report.date, report.project, report.description, report.duration, report.overtime])
            return response
    else:
        users = User.objects.exclude(username__in =['admin'])
        context = {
            'users': users
        }
        return render(request, 'timesheet_app/report.html', context)

    
def delete(request, id):
    Report.objects.get(id=id).delete()
    return redirect('timesheet')

def edit(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        # date = request.POST['date']
        project = request.POST['project']
        duration = request.POST['duration']
        overtime = request.POST['overtime']
        description = request.POST['description']
        
        report = Report.objects.filter(id=id).update(name=name, project=project, duration=duration, overtime=overtime, description=description)

        return redirect('timesheet')
    else:
        report = Report.objects.get(id=id)
        context = {
            'report': report
        }
    return render(request, 'timesheet_app/edit.html', context)

