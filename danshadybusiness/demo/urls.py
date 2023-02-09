from django.urls import path
from . import views

app_name = 'demo'
urlpatterns = [
    path('', views.index, name='Login'),
    path('loggedIn', views.loggedIn, name='Logged_In'),
    path('logoutView', views.logoutView, name='logoutView'),
    path('cars', views.cars, name='cars'),
    path('addCar', views.addCar, name='addCar')
]