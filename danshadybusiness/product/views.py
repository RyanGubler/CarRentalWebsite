from django.shortcuts import render
from product.models import CustomUser, Car, ServiceTicket
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.models import Group, Permission, User
from datetime import datetime




# We may want to pass context back to the addFunds paget that shows
# the current total funds in account.

def addFunds(request):
    # customUser = CustomUser.objects.get(user = request.user)
    # if request.method == "POST":
    #     if '$10' in request.method.POST:
    #         customUser.addFunds(10)
    #     elif '$25' in request.method.POST:
    #         customUser.addFunds(25)
    #     elif '$50' in request.method.POST:
    #         customUser.addFunds(50)
    #     elif '$100' in request.method.POST:
    #         customUser.addFunds(100)
    #     else:
    #         customUser.addFunds(float(request.POST('custom')))
    return render(request, 'product/addFunds.html', {})



def aboutUs(request):
    return render(request, 'product/aboutUs.html', {})

def index(request):
    return render(request, 'product/index.html', {})

# def login(request):
#     return render(request, 'product/login.html', {})

def signup(request):
    return render(request, 'product/signup.html', {})

def service(request):
    return render(request, 'product/serviceTicket.html', {})

def reservation(request):
    return render(request, 'product/reservation.html', {})

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

def logoutPage(request):
        logout(request)
        return redirect(reverse('product:loginTest'))

@login_required(login_url='product:loginTest')
def customUser(request):
    customUser = CustomUser.objects.get(user = request.user)
    return render(request, 'product/customUser.html', {'customUser': customUser})



def addCarPage(request):
    if not request.user.has_perm('Manager'):
        return redirect(reverse('product:customUser'))

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



def availableCars(request):
    resp = {}
    startDate = request.GET.get('startDate')
    endDate = request.GET.get('endDate')
    startDate = datetime.strptime(startDate, '%Y-%m-%d').date()
    endDate = datetime.strptime(endDate, '%Y-%m-%d').date()
    print("The start date converted to a string is: "+ str(startDate))
    if startDate> endDate:
        resp['error'] = "End Date is before Start Date"
        return JsonResponse(resp)
    for car in Car.objects.all():
        addingCar = True
        if len(car.carreservation_set.all()) == 0:
            resp[car.name] = car.price
        else:
            for reservation in car.carreservation_set.all():
                if startDate <= reservation.endDate and startDate >= reservation.startDate:
                    addingCar = False
                    break
                if endDate >= reservation.startDate and endDate <= reservation.endDate:
                    addingCar = False
                    break
            if addingCar:
                resp[car.id] = car.name
    return JsonResponse(resp)




def createTicket(request):
    customerId = request.POST['customerId']
    carId = request.POST['carId']
    ticket = ServiceTicket(customerId=customerId, carId=carId)
    ticket.save()

def terminate(request):
    serviceTicketId = request.POST['serviceTicketId']
    ServiceTicket.objects.filter(pk=serviceTicketId)

def service(request):
    ticketList = list[ServiceTicket.objects.all()[:5]]
    return render(request, 'product/serviceTicket.html', {'ticketList' : ticketList})

def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(username = request.POST['email'],
                                        password = request.POST['password'], 
                                        email = request.POST['email'], 
                                        first_name = request.POST['firstName'], 
                                        last_name = request.POST['lastName'])
        user.save
        return render(request, 'product/login.html', {})
    return render(request,'product/signup.html', {})

