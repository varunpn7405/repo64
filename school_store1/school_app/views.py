from django.contrib import auth,messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
def home(request):
    return render(request, 'home.html')
def msg(request):
    return render(request, 'msg.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'new.html')
        else:
            messages.info(request,'invalid credentials!!')
    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already taken!!")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                return render(request, 'login.html')
                user.save();
        else:
            messages.info(request, "password not matching!!")
    return render(request, 'register.html')
def new_page(request):
    return render(request, 'new.html')
def form(request):
    return render(request,'form.html')
def navdrop(request):
    return render(request,'navdrop.html')
