from django.shortcuts import render
from product.models import CustomUser

def addFunds(request):
    
    return render(request, 'product/addFunds.html', {})

# Create your views here.
