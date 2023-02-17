from django.shortcuts import render

def addFunds(request):
    return render(request, 'product/addFunds.html', {})

def aboutUs(request):
    return render(request, 'product/aboutUs.html', {})

# Create your views here.
