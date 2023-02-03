from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Login'),
    path('loggedIn', views.loggedIn, name='Logged_In')
]