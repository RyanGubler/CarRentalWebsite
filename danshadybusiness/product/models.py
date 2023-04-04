from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver




class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    balance = models.FloatField(default = 0.0)
    hours = models.FloatField(default = 0.0)

    def addFunds(self,amount):
        self.balance += amount
    
    def addHours(self,amount):
        self.hours += amount
    
    def __str__(self):
        return self.user.username
    

#this method is to create CustomUser when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)

#this method to update profile when user is updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customuser.save()


class Car(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()

    def __str__(self):
        return self.name
    

class CarReservation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    startDate = models.DateField()
    endDate = models.DateField()
    lojacked = models.BooleanField(default=False)
    insurance = models.BooleanField(default=False)


    def __str__(self):
        return "User: "+self.user.user.username +" Car: "+self.car.name+ " ("+str(self.startDate) + " -> " + str(self.endDate) + ")"



# Create your models here.

class ServiceTicket(models.Model):
    customerId = models.IntegerField()
    carId = models.IntegerField()
    assigned = models.BooleanField(default=False)

    def __str__(self):
        return User.objects.get(pk=self.customerId).username + ' '+ str(Car.objects.get(pk = self.carId))

