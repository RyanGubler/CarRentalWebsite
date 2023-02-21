from django.shortcuts import render
from product.models import CustomUser, Car
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import JsonResponse





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

def logoutPage(request):
        logout(request)
        return redirect(reverse('product:loginTest'))

@login_required
def customUser(request):
    customUser = CustomUser.objects.get(user = request.user)
    return render(request, 'product/customUser.html', {'customUser': customUser})



def addCarPage(request):
    context = CustomUser.objects.get(user=request.user)
    return render(request, 'product/addCarPage.html', {'context':context})


def addCar(request):
    customUser = CustomUser.objects.get(user = request.user)
    if customUser.balance < float(request.POST['carPrice']):
        return render(request, 'product/addCarPage.html', {'errorMessage': "Insufficient funds, cannot purchase car"})


    customUser.addFunds(float(request.POST['carPrice']) * -1)
    customUser.save()
    car = Car(name = request.POST['carName'], price = float(request.POST['carPrice']) / 10)
    car.save()
    return redirect(reverse('product:addCarPage'))



# def availableCars(request):
#     resp = {}
#     startDate = request.GET.get('startDate')
#     endDate = request.GET.get('endDate')

#     for car in Car.objects.all():
#         addingCar = True
#         if len(car.carreservation_set.all()) == 0:
#             resp[car.name] = car.price
#         else:
#             for reservation in car.carreservation_set.all():
#                 if startDate < reservation.endDate and startDate > reservation.startDate:
#                     addingCar = False
#                     break
#                 if endDate > reservation.startDate and endDate < reservation.endDate:
#                     addingCar = False
#                     break
#             if addingCar:
#                 resp[car.name] = car.price
#     return JsonResponse(resp)






