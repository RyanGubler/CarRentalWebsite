from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('addFunds', views.addFunds, name='addFunds'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
]