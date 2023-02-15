from django.db import models

# Create your models here.

class Car(models.Model):
    color = models.CharField(max_length=20)


