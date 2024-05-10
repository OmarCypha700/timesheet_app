from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'employee_id', 'tel')})
UserAdmin.fieldsets= tuple(fields)
admin.site.register(CustomUser, UserAdmin)
