from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name = "login"),
    path('addFunds/', views.addFunds, name='addFunds'),
    path('signup/', views.signup, name= "signup"),
]