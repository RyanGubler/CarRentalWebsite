from django.urls import path
from . import views

urlpatterns = [
    path('addFunds/', views.addFunds, name='addFunds'),

    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('service/', views.service, name='service'),

]