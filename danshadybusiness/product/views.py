from django.shortcuts import render

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
