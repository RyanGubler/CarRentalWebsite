from django.urls import path
from . import views


urlpatterns = [
<<<<<<< HEAD
    path('index', views.index, name='index'),
    path('addFunds', views.addFunds, name='addFunds'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
=======
    path('addFunds/', views.addFunds, name='addFunds'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('service/', views.service, name='service'),
>>>>>>> c58b73284041de7667ebdfd4204eaad8c01cce84
]