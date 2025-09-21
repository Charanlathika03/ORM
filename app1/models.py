from django.db import models
from django.contrib import admin

# Create your models here.

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)      
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"