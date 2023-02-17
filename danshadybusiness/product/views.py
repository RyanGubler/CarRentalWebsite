from django.shortcuts import render
from product.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User




def addFunds(request):
    return render(request, 'product/addFunds.html', {})

# Create your views here.
# @login_required
# def index(request):
#     customUser = CustomUser.objects.get(user = request.user)
#     return render(request, 'product/index.html',{'customUser': customUser})




def loginTest(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(reverse('product:customUser'))
        
        else:
            context = {'errorMessage': "Invalid login credentials, please try again!"}
            return render(request, 'product/login.html', context)

        # Return an 'invalid login' error message.

    
    return render(request, 'product/login.html')


def signup(request):
    if request.method == "POST":
        user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'], email=request.POST['password'], firstname = request.POST['firstName'], lastname = request.POST['lastName'])
        return redirect(reverse('product:loginTest'))

    return render(request, 'product/signup.html')

def logout(request):
        logout(request)
        return redirect(reverse('product:loginTest'))


def customUser(request):
    customUser = CustomUser.objects.get(user = request.user)
    return render(request, 'product/customUser.html', {'customUser': customUser})

