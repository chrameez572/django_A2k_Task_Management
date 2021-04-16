from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import EmployeeRegister,CreationUserForm
from .models import Employee
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):

    return render(request,'index.html')

def login (request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request, user)
            return redirect('addandshow')
        else:
            messages.info(request, 'Username or Password is Incorrect')
    return render(request, 'login.html' )

def register (request):
    form = CreationUserForm()
    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
           form.save()
           user = form.cleaned_data.get('username')
           messages.success(request, ' Account Created Sucessfully for ' + user)
           return redirect('login')

    return render(request, 'register.html',{'form':form})
def logout (request):
    # logout(request)
    return redirect('login')

@login_required(login_url='login')
def add_show(request):
    if request.method == 'POST':
        form = EmployeeRegister(request.POST)
        if form.is_valid():
            form.save()
        form = EmployeeRegister()
    else:
        form = EmployeeRegister()
    table_data = Employee.objects.all()
    return render(request, 'addandshow.html', {'form':form,'data':table_data} )



def delete_data(request,id):
    if request.method == 'POST':
        data = Employee.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')



def update_data(request,id):
    if request.method == 'POST':
        data = Employee.objects.get(pk=id)
        form = EmployeeRegister(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:
        data = Employee.objects.get(pk=id)
        form = EmployeeRegister(instance=data)

    return render(request, 'update.html', {'form':form})


