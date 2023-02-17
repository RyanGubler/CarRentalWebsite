from django.urls import path
from . import views

urlpatterns = [
    path('addFunds/', views.addFunds, name='addFunds'),
    path('service/', views.service, name='service')
]