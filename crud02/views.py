from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import crudSerializer
from .forms import EmployeeForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        Username=request.POST['username']
        Email=request.POST['Email']
        city=request.POST['city']
        address=request.POST['address']
        pincode=request.POST['pincode']
        password=request.POST['Password']
        
        
        log=customer(name=Username, Email=Email, city=city, address=address, pincode=pincode, password=password)
        
        log.save()
    
    return render(request, 'register.html')

def  loginpage(request):
    if request.method == 'POST':
        Email = request.POST.get('email')
        password = request.POST.get('password')
        user=customer.objects.filter(Email=Email, password=password)
        print(Email)
        print(password)
        if user.exists():
            return HttpResponse("Successfully run")
        else:   
            return HttpResponse("404 error!")
           
    return render(request,"login.html")

def employees_list(request):
    employee = Employee.objects.all()
    return render(request, 'list.html', {"employees":employee})


def create_employee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'form': form,
    }
    return render(request, 'create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'edit.html', context)


def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employees-list')

    context = {
        'employee': employee,
    }
    return render(request, 'delete.html', context)