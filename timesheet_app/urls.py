from django.urls import path
from .import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.timesheet, name='timesheet'),
    path('report/', views.report, name='report'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
]