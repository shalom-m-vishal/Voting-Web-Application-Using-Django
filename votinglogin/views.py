from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from votinglogin.models import loginForm

def home(request):
    if request.method == 'POST':
        login=loginForm()
        username = request.POST.get('username')
        password = request.POST.get('password')
        login.username=username
        login.password=password
        login.save()
        return render(request,'homepage.html')    
    return render(request, 'loginpage.html')
    