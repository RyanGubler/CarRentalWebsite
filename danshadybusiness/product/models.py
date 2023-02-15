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
    
    

    

#this method is to create CustomUser when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)

#this method to update profile when user is updated
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.customuser.save()



