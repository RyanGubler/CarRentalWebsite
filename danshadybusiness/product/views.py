from django.shortcuts import render
from django.contrib.auth.models import Group, Permission, User
from django.contrib.auth import authenticate, login
from .models import ServiceTicket
def addFunds(request):
    return render(request, 'product/addFunds.html', {})

<<<<<<< HEAD
def aboutUs(request):
    return render(request, 'product/aboutUs.html', {})

def index(request):
    return render(request, 'product/index.html', {})

=======
def login(request):
    return render(request, 'product/login.html', {})

def signup(request):
    return render(request, 'product/signup.html', {})

def service(request):
    return render(request, 'product/serviceTicket.html', {})
>>>>>>> c58b73284041de7667ebdfd4204eaad8c01cce84
# Create your views here.

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
        user = User.objects.create_user(username = request.POST['username'],
                                        password = request.POST['password'], 
                                        email=request.POST['email'], 
                                        firstname = request.POST['firstName'], 
                                        lastname = request.POST['lastName'])
        return(request, 'product/login.html', {})
    return render(request,'product/signup.html', {})