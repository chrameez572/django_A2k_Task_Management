from django import forms
from .models import Employee
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class EmployeeRegister(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Task_Name','Task_Discription']
        widgets = {
            'Task_Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Task_Discription': forms.TextInput(attrs={'class': 'form-control'}),

        }


class CreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),

        }