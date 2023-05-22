from django.shortcuts import render

# Create your views here.

from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')


def contato(request):
    return HttpResponse("contato")

def sobre(request):
    return HttpResponse("sobre")

urlpatterns =[
    path('admin/', admin.site.urls),
    path('',home),
    path('contato/',contato),
    path('sobre/',sobre), 
    ]