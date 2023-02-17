from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('addFunds/', views.addFunds, name='addFunds'),
    path('aboutUs/', views.aboutUs, name='aboutUs'),
]