from django.db import models

# Create your models here.

class ServiceTicket(models.Model):
    customerId = models.IntegerField()
    carId = models.IntegerField()
    assigned = models.BooleanField(default=False)