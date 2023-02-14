from django.urls import path
from . import views

urlpatterns = [
    path('addFunds/', views.addFunds, name='addFunds'),
]