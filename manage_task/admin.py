from django.contrib import admin
from .models import Employee
# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id','Task_Name','Task_Discription','Created_Time','Updated_Time')
