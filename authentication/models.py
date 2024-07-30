from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    # tel = models.IntegerField(default=0)
    staff_code = models.CharField(max_length=2, default='')
