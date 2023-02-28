from django.contrib import admin
from .models import CustomUser, Car, CarReservation, ServiceTicket
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(CarReservation)
admin.site.register(Car)
admin.site.register(ServiceTicket)