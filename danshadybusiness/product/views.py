from django.shortcuts import render
from .models import ServiceTicket
def addFunds(request):
    return render(request, 'product/addFunds.html', {})

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