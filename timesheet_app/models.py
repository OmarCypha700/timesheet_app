from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Report(models.Model):
    name = models.CharField(max_length=100, default='')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    project = models.CharField(max_length=50)
    duration = models.IntegerField(null=False, blank=False)
    overtime = models.IntegerField(null=True, default=0)
    description = models.TextField(default="")
    staff_code = models.CharField(max_length=2, default='')
    
    def __str__(self):
        return self.name


