from django.urls import path
from . import views
app_name = 'product'

urlpatterns = [
    path('', views.loginTest, name = "loginTest"),
    path('addFunds/', views.addFunds, name='addFunds'),
    path('signup/', views.signup, name= "signup"),
    path('customUser/', views.customUser, name = "customUser"),
]