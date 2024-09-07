from django.db import models

# Create your models here.

#placeholder class for each Restaurant
class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    address_link = models.CharField(max_length=50)
    cuisine_type = models.CharField(max_length=50) #potentially an enum
    rating = models.IntegerField()
    contact = models.CharField(max_length=50)