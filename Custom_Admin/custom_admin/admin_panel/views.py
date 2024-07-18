# admin_panel/views.py

from django.shortcuts import render

def adminpanel(request):
    # Add dashboard logic here
    return render(request, 'admin_panel/adminpanel.html')

def login(request):
    # Add user list logic here
    return render(request, 'admin_panel/Login.html')

def register(request):
    # Add user detail logic here
    return render(request, 'admin_panel/Register.html')

def userhome(request):

    return render(request,'admin_panel/userhome.html')

def homepage(request):
    return render(request, 'admin_panel/home.html')