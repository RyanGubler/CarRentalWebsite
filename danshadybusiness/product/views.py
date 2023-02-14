from django.shortcuts import render

def addFunds(request):
    return render(request, 'product/addFunds.html', {})

# Create your views here.
