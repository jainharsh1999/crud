from django.shortcuts import render
from .models import *
from django.http import HttpResponse, Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import crudSerializer

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

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:k>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:k>/',
		'Delete':'/task-delete/<str:k>/',
		}
	return Response(api_urls)

@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('id')
	serializer = crudSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = crudSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = crudSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = crudSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')