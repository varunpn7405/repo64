from django.contrib import auth,messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
def home(request):
    return render(request, 'home.html')
def msg(request):
    return render(request, 'msg.html')
def login_view(request):
    return render(request, 'login.html')
def register(request):
        return render(request, 'register.html')
def new_page(request):
    return render(request, 'new.html')
def form(request):
    return render(request,'form.html')
def navdrop(request):
    return render(request,'navdrop.html')
