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



@login_required(login_url='product:loginTest')
def addFunds(request):
    customUser = CustomUser.objects.get(user = request.user)
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

    return render(request, 'product/addFunds.html', {'customUser': customUser})


@login_required(login_url='product:loginTest')
def aboutUs(request):
    return render(request, 'product/aboutUs.html', {})

@login_required(login_url='product:loginTest')
def index(request):
    customUser = CustomUser.objects.get(user = request.user)
    return render(request, 'product/index.html', {'customUser': customUser})
@login_required(login_url='product:loginTest')
def reservation(request):
    return render(request, 'product/reservation.html', {})

@login_required(login_url='product:loginTest')
def hire(request):
    return render(request, 'product/hire.html', {})

@login_required(login_url='product:loginTest')
def account(request):
    now = date.today()
    customUser = CustomUser.objects.get(user = request.user)
    list = []
    for reservation in customUser.carreservation_set.all():
        if reservation.endDate >= now:
            list.append(reservation)
    return render(request, 'product/account.html', {'customUser': customUser,'reservations':list})

def loginTest(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect(reverse('product:account'))
        
        else:
            context = {'errorMessage': "Invalid login credentials, please try again!"}
            return render(request, 'product/login.html', context)
    if request.user.is_authenticated:
        return redirect(reverse('product:account'))

    
    return render(request, 'product/login.html')

@login_required(login_url='product:loginTest')
def logoutPage(request):
        logout(request)
        return redirect(reverse('product:loginTest'))

@login_required(login_url='product:loginTest')
def addCarPage(request):
    if not request.user.has_perm('auth.Manager'):
        return redirect(reverse('product:account'))

    context = CustomUser.objects.get(user=request.user)
    return render(request, 'product/addCarPage.html', {'context':context})

@login_required(login_url='product:loginTest')
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
            resp[str(car.id)] = car.name
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
                resp[str(car.id)] = car.name
                
    response = JsonResponse(resp)
    response['Access-Control-Allow-Origin'] = '*'

    return response

@login_required(login_url='product:loginTest')
def createTicketPage(request):
    # take an integer in a post
    # passes context with list of all current reservations in appropriate date window
    if request.method =='POST':
        reservation = CarReservation.get(id=request.POST['reservationId'])
        createTicket(CarReservation.meta.get_field('customerId'), CarReservation.meta.get_field('carId'))
    currentDate = date.today()
    validReservations = CarReservation.objects.exclude(startDate__gte=currentDate)
    return render(request, 'product/createTicketPage.html', {'validReservations' : validReservations})

@login_required(login_url='product:loginTest')
def createTicket(customerId, carId):
    ticket = ServiceTicket(customerId=customerId, carId=carId)
    ticket.save()

def terminate(request):
    serviceTicketId = request.POST['serviceTicketId']
    ServiceTicket.objects.filter(pk=serviceTicketId)

@login_required(login_url='product:loginTest')
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
    return render(request, 'product/serviceTicket.html', {'ticketList' : ticketList})

def deleteTickets(deleteList):
    ticketList = ServiceTicket.objects.all()
    firstTickets = []
    if len(ticketList) <= 3:
        firstTickets = ticketList
    else:
        firstTickets = ticketList[:3]
    for i in range(len(firstTickets)):
        if deleteList[i] == "on":
            customUserId = firstTickets[i].customerId
            customUser = CustomUser.objects.get(pk = customUserId)
            customUser.addFunds(-300.0)
            customUser.save()
            firstTickets[i].delete()


def signup(request):
    if request.method == 'POST':
        try:
            exists = CustomUser.objects.get(email = request.POST['email'])
            return render(request,"product/signup.html",{'error':"Email already exists"})
        except:
            user = User.objects.create_user(username = request.POST['email'],
                                            password = request.POST['password'], 
                                            email = request.POST['email'], 
                                            first_name = request.POST['firstName'], 
                                            last_name = request.POST['lastName'])
            user.save
            user.groups.add(Group.objects.get(name='User'))
            return render(request, 'product/login.html', {})
    return render(request,'product/signup.html', {})


@login_required(login_url='product:loginTest')
def employeeHours(request):
    if request.user.has_perm('auth.Employee'):
        return render(request,'product/reportHours.html')

    else:
        return redirect(reverse('product:account'))
    
@login_required(login_url='product:loginTest')
def logHours(request):
    if request.method == 'POST' and request.user.has_perm('auth.Employee'):
        totalHours = request.POST['hours']
        user = CustomUser.objects.get(user = request.user)
        user.addHours(float(totalHours))
        user.save()
        return redirect(reverse('product:account'))
    return redirect(reverse('product:employeeHours'))



@login_required(login_url='product:loginTest')
def payEmployeePage(request):
    if request.user.has_perm('auth.Manager'):
        employees = []
        for employee in User.objects.all():
            if employee.has_perm('auth.Employee'):
                if employee.has_perm('is super user'):
                    continue
                employees.append(employee)
        print(employees)
        return render(request, 'product/payEmployeePage.html', {'employees':employees})
    return redirect(reverse('product:account'))

@login_required(login_url='product:loginTest')
def payAll(request):
    if request.method == "POST" and request.user.has_perm('auth.Manager'):
        for user in CustomUser.objects.all():
            user1 = user.user
            if user1.has_perm('auth.Employee'):
                hours = user.hours
                user.addFunds(float(hours*15.0))
                user.addHours(float(hours*-1))
                user.save()
        return redirect(reverse('product:account'))
    return redirect(reverse('product:account'))



@login_required(login_url='product:loginTest')
def displayCar(request, car_id, startDate, endDate):
    
    car = Car.objects.get(pk=car_id)
    customUser = CustomUser.objects.get(user = request.user)
    start = datetime.strptime(startDate, '%Y-%m-%d').date()
    end = datetime.strptime(endDate, '%Y-%m-%d').date()

    return render(request, 'product/displayCar.html', {'car':car,'startDate': startDate, 'endDate':endDate, 'customUser':customUser, 'totalPrice': ((end-start).days +1)*car.price})

@login_required(login_url='product:loginTest')
def reserveCar(request, car_id):
    car = Car.objects.get(pk=car_id)
    customUser = CustomUser.objects.get(user = request.user)
    startDate = request.POST['startDate']
    endDate = request.POST['endDate']
    insurance = request.POST['insurance']

    if insurance == "Yes":
        insurance = 50.0
        # lojacked = False
    else:
        insurance = 0.0
        # lojacked = True
    start = datetime.strptime(startDate, '%Y-%m-%d').date()
    end = datetime.strptime(endDate, '%Y-%m-%d').date()
    if customUser.balance < ((float((end - start).days +1)*car.price) + insurance):
        return redirect('product:displayCar', startDate = startDate, endDate = endDate, car_id = car_id)

    customUser.addFunds(-((float((end - start).days +1)*car.price) + insurance))
    customUser.save()
    if insurance == 50.0:

        reservation = CarReservation(car = car, user = customUser, startDate = request.POST['startDate'], endDate = request.POST['endDate'], lojacked = False, insurance = True)
    else:
        reservation = CarReservation(car = car, user = customUser, startDate = request.POST['startDate'], endDate = request.POST['endDate'], lojacked = False, insurance = False)

    reservation.save()


    # if lojacked:
    #     ticket = ServiceTicket(customerId = customUser.id, carId = car.id)
    #     ticket.save()
    #     customUser.addFunds(-300)
    #     customUser.save()
    
    return redirect(reverse('product:account'))

@login_required(login_url='product:loginTest')  
def hirePage(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.POST['email'])
        hire(user,request.POST['position'].capitalize() )
    return render(request, 'product/hire.html', context={
        'users' : User.objects.all
    })

def hire(user, position):
    if position not in user.groups.all():
        user.groups.add(Group.objects.get(name= position))
        user.save()


@login_required(login_url='product:loginTest')
def inventory(request):
    Cars = Car.objects.all()
    return render(request,'product/inventory.html', {'Cars':Cars})


@login_required(login_url='product:loginTest')
def overdueReservations(request):
    if not request.user.has_perm('auth.Manager'):
        return redirect(reverse('product:account'))
    reservations = []
    now = date.today()
    for reservation in CarReservation.objects.all():
        if (reservation.endDate < now) and (not reservation.lojacked):
            reservations.append(reservation)
        elif (not reservation.insurance) and (not reservation.lojacked):
            reservations.append(reservation)
    return render(request, 'product/createTicketPage.html', {'reservations':reservations})

@login_required(login_url='product:loginTest')
def lojackCar(request):
    if request.method == "POST" and request.user.has_perm('auth.Manager'):
        reservation_id = request.POST['options']
        reservation = CarReservation.objects.get(pk = reservation_id)
        customUser = reservation.user
        reservation.lojacked = True
        ticket = ServiceTicket(customerId = customUser.user.id, carId = reservation.car.id)
        ticket.save()
        reservation.save()
        customUser.save()
        return redirect(reverse('product:overdueReservations'))
    return redirect(reverse('product:account'))


