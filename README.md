# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from Car Inventory Database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM
<img width="940" height="506" alt="image" src="https://github.com/user-attachments/assets/5915ca50-62bd-46c4-b63f-6ace33c4b2cc" />



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

**models.py**
```python
from django.db import models
from django.contrib import admin

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)      
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"
```
**admin.py**
```python
from django.contrib import admin
from .models import Movies, MoviesAdmin
# Register your models here.
admin.site.register(Movies, MoviesAdmin)

from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'brand', 'model', 'year', 'price')
    search_fields = ('brand', 'model')
    list_filter = ('year',)
```

## OUTPUT

<img width="1919" height="1110" alt="image" src="https://github.com/user-attachments/assets/6a0547a2-5777-4e5f-812e-b3a007c3d52b" />



## RESULT
Thus the program for creating a database using ORM hass been executed successfully
