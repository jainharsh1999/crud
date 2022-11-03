"""crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud02.views import *
from . import views

urlpatterns = [
    
    path('register', register, name='register'),
    path('loginpage', loginpage, name='loginpage'),
    path('', views.apiOverview, name="api-overview"),
	path('/task-list/', views.taskList, name="taskList"),
	path('/task-detail/<str:k>/', views.taskDetail, name="taskDetail"),

	path('/task-create/', views.taskCreate, name="taskCreate"),
	path('/task-update/<str:k>/', views.taskUpdate, name="taskUpdate"),
	path('/task-delete/<str:k>/', views.taskDelete, name="taskDelete"),
 
]
    
    

