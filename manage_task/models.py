from django.db import models

# Create your models here.
class Employee(models.Model):
    Task_Name = models.CharField(max_length=15, null=False, blank=False)
    Task_Discription = models.CharField(max_length=50, null=False, blank=False)
    Created_Time = models.DateTimeField(auto_now_add=True, blank=False)
    Updated_Time = models.DateTimeField(auto_now=True)