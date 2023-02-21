from django.shortcuts import render

def addFunds(request):
    return render(request, 'product/addFunds.html', {})

def login(request):
    return render(request, 'product/login.html', {})

def signup(request):
    return render(request, 'product/signup.html', {})

def service(request):
    return render(request, 'product/serviceTicket.html', {})
# Create your views here.
