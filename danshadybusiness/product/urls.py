from django.urls import path
from . import views
app_name = 'product'


urlpatterns = [

    path('', views.loginTest, name = "loginTest"),
    path('addFunds/', views.addFunds, name='addFunds'),
    path('customUser/', views.customUser, name = "customUser"),
    path('addCarPage/', views.addCarPage, name = 'addCarPage'),
    path('addCarPage/addCar/',views.addCar, name='addCar'),
    path('index/', views.index, name='index'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('service/', views.service, name='service'),
    path('availableCars/', views.availableCars, name="availableCars"),
    path('customUser/logout/', views.logoutPage, name = "logoutPage"),

]