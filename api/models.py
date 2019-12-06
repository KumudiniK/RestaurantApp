from django.db import models

# Create your models here.
class Restaurant(models.Model):
    Rname = models.CharField(max_length=200)
    address=models.CharField(max_length=200)

class Items(models.Model):
     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
     item = models.CharField(max_length=200)
     price=models.IntegerField(default=0)