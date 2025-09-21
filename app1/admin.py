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
