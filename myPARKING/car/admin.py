"""
Parking User Admin page
"""
from django.contrib import admin

from .models import Car
from .models import Vehicles

class CarAdmin(admin.ModelAdmin):
    """
    Special admin class to put owners inline
    """
    model = Car
    filter_horizontal = ('owners',)

admin.site.register(Vehicles)
admin.site.register(Car, CarAdmin)
