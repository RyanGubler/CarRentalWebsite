from django.shortcuts import render

def addFunds(request):
    return render(request, 'product/addFunds.html', {})

def aboutUs(request):
    return render(request, 'product/aboutUs.html', {})

def index(request):
    return render(request, 'product/index.html', {})

# Create your views here.
