from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from .models import Car


# Create your views here.

def index(request):
    if request.method == "POST":
        username = request.POST['user_name_input']
        password = request.POST['user_password_input']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect(reverse('demo:Logged_In'))
        else:
            return render(request, 'authenticate/login.html')
    return render(request, 'authenticate/login.html')

@login_required
def loggedIn(request):
    return render(request, 'authenticate/logged_in.html')


@login_required
def cars(request):
    carTotal = Car.objects.all().count()
    context = {
        'total': carTotal,
    }
    return render(request, 'authenticate/cars.html', context)

def addCar(request):
    c = Car(color='red')
    c.save()
    return redirect(reverse('demo:cars'))

def logoutView(request):
    logout(request)
    return redirect(reverse('demo:Login'))