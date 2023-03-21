from django.shortcuts import render
from product.models import CustomUser, Car, ServiceTicket, CarReservation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.models import Group, Permission, User
from datetime import datetime, date
from .forms import ServiceForm




def addFunds(request):
    customUser = CustomUser.objects.get(user = request.user)
    print(request.POST)
    if request.method == 'POST':
        if "10" in request.POST:
            customUser.addFunds(10.0)
            customUser.save()
            return redirect(reverse("product:addFunds"))
        elif "25" in request.POST:
            customUser.addFunds(25.0)
            customUser.save()
            return redirect(reverse("product:addFunds"))
        elif "50" in request.POST:
            customUser.addFunds(50.0)
            customUser.save()
            return redirect(reverse("product:addFunds"))
        elif "100" in request.POST:
            customUser.addFunds(100.0)
            customUser.save()
            return redirect(reverse("product:addFunds"))
        elif "custom" in request.POST:
            customUser.addFunds(float(request.POST["custom"]))
            customUser.save()
            return redirect(reverse("product:addFunds"))

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

def hire(request):
    return render(request, 'product/hire.html', {})

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
    
    # check if user is already logged in
    if request.user.is_authenticated:
        return redirect(reverse('product:customUser'))

    
    return render(request, 'product/login.html')

def logoutPage(request):
        logout(request)
        return redirect(reverse('product:loginTest'))

@login_required(login_url='product:loginTest')
def customUser(request):
    customUser = CustomUser.objects.get(user = request.user)
    return render(request, 'product/account.html', {'customUser': customUser})



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
    car = Car(name = request.POST['carName'], price = float(request.POST['carPrice']))
    car.save()
    return redirect(reverse('product:addCarPage'))



def availableCars(request):
    resp = {}
    try:
        startDate = request.GET.get('startDate')
        endDate = request.GET.get('endDate')
        carPrice = request.GET.get('carPrice')
        startDate = datetime.strptime(startDate, '%Y-%m-%d').date()
        endDate = datetime.strptime(endDate, '%Y-%m-%d').date()
    except:
        resp['error'] = "Please Input Start and End Date"
        return JsonResponse(resp)
    if startDate> endDate:
        resp['error'] = "End Date is before Start Date"
        return JsonResponse(resp)
    resp['start-date'] = startDate
    resp['end-date'] = endDate
    for car in Car.objects.all():
        addingCar = True
        if car.price != float(carPrice):
            continue
        if len(car.carreservation_set.all()) == 0 and car.price == float(carPrice):
            resp[car.name] = car.id
        else:
            for reservation in car.carreservation_set.all():
                if (startDate <= reservation.endDate and startDate >= reservation.startDate) or (car.price != float(carPrice)):
                    addingCar = False
                    break
                if (endDate >= reservation.startDate and endDate <= reservation.endDate) or (car.price != float(carPrice)):
                    addingCar = False
                    break
                if (reservation.startDate >= startDate and reservation.startDate <= endDate) or (car.price != float(carPrice)):
                    addingCar = False
                    break
                if (reservation.endDate >= startDate and reservation.endDate <= endDate) or (car.price != float(carPrice)):
                    addingCar = False
                    break
            if addingCar:
                resp[car.name] = car.id
    response = JsonResponse(resp)
    response['Access-Control-Allow-Origin'] = '*'

    return response




def createTicket(request):
    customerId = request.POST['customerId']
    carId = request.POST['carId']
    ticket = ServiceTicket(customerId=customerId, carId=carId)
    ticket.save()

def terminate(request):
    serviceTicketId = request.POST['serviceTicketId']
    ServiceTicket.objects.filter(pk=serviceTicketId)

def service(request):

    if request.method == 'POST':
        deleteList = []
        deleteList.append(request.POST.get('1st'))
        deleteList.append(request.POST.get('2nd'))
        deleteList.append(request.POST.get('3rd'))
        deleteTickets(deleteList)
    ticketList = ServiceTicket.objects.all()
    firstTickets = []
    if len(ticketList)<= 3:
        firstTickets = ticketList
    else :
        firstTickets = ticketList[:3]
    form = ServiceForm()
    return render(request, 'product/serviceTicket.html', {'ticketList' : ticketList, 'form': form})

def deleteTickets(deleteList):
    ticketList = ServiceTicket.objects.all()
    firstTickets = []
    if len(ticketList) <= 3:
        firstTickets = ticketList
    else:
        firstTickets = ticketList[:3]
    for i in range(len(firstTickets)):
        if deleteList[i] == "on":
            firstTickets[i].delete()

def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(username = request.POST['email'],
                                        password = request.POST['password'], 
                                        email = request.POST['email'], 
                                        first_name = request.POST['firstName'], 
                                        last_name = request.POST['lastName'])
        user.save
        user.groups.add(Group.objects.get(name='User'))
        return render(request, 'product/login.html', {})
    return render(request,'product/signup.html', {})



def employeeHours(request):
    if request.user.has_perm('auth.Employee'):
        return render(request,'product/employeeHours.html')

    else:
        return redirect(reverse('product:customUser'))
    

def logHours(request):
    if request.method == 'POST' and request.user.has_perm('auth.Employee'):
        totalHours = request.POST['hours']
        user = CustomUser.objects.get(user = request.user)
        user.addHours(float(totalHours))
        user.save()
        return redirect(reverse('product:customUser'))
    return redirect(reverse('product:employeeHours'))




def payEmployeePage(request):
    if request.user.has_perm('auth.Manager'):
        return render(request, 'product/payEmployeePage.html')
    return redirect(reverse('product:customUser'))


def payAll(request):
    if request.method == "POST" and request.user.has_perm('auth.Manager'):
        for user in CustomUser.objects.all():
            user1 = user.user
            if user1.has_perm('auth.Employee'):
                hours = user.hours
                user.addFunds(float(hours*15.0))
                user.addHours(float(hours*-1))
                user.save()
        return redirect(reverse('product:customUser'))
    return redirect(reverse('product:customUser'))




def displayCar(request, car_id, startDate, endDate):
    car = Car.objects.get(pk=car_id)
    customUser = CustomUser.objects.get(user = request.user)
    return render(request, 'product/displayCar.html', {'car':car,'startDate': startDate, 'endDate':endDate, 'customUser':customUser})

def reserveCar(request, car_id):
    car = Car.objects.get(pk=car_id)
    customUser = CustomUser.objects.get(user = request.user)
    reservation = CarReservation(car = car, user = customUser, startDate = request.POST['startDate'], endDate = request.POST['endDate'], lojacked = False)
    reservation.save()
    return redirect(reverse('product:customUser'))
    
def hirePage(request):
    if request.method == 'POST':
        # print(request.POST['position'])
        # print(type(request.POST['position']))
        user = User.objects.get(email=request.POST['email'])
        # print(user.groups.get(request.POST['position']))
        hire(user,request.POST['position'].capitalize() )
    return render(request, 'product/hire.html', context={
        'users' : User.objects.all
    })
def hire(user, position):
    if position not in user.groups.all():
        user.groups.add(Group.objects.get(name= position))
        user.save()

