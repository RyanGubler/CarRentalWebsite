from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST['user_name_input']
        password = request.POST['user_password_input']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("Logged_In")
        else:
            return render(request, 'authenticate/login.html')
    return render(request, 'authenticate/login.html')
def loggedIn(request):
    return render(request, 'authenticate/logged_in.html')