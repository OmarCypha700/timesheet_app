from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # project = models.CharField(max_length=100, default='')
    employee_id = models.CharField(max_length=10, default='')
    tel = models.IntegerField(default=0)
    staff_code = models.CharField(max_length=2, default='')
