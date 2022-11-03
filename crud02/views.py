from django.shortcuts import render
from .models import *
from django.http import HttpResponse, Http404


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