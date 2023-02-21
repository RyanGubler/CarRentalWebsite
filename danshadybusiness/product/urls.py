from django.urls import path
from . import views


urlpatterns = [

    path('index', views.index, name='index'),
    path('addFunds', views.addFunds, name='addFunds'),
    path('aboutUs', views.aboutUs, name='aboutUs'),


    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('service/', views.service, name='service'),
]