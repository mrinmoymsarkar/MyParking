"""
Parking User Admin page
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import ParkingUser

admin.site.register(ParkingUser)

class ParkingUserInline(admin.StackedInline):
    """
    Set Parking User Admin to be inline
    """
    model = ParkingUser
    can_delete = False

class UserAdmin(BaseUserAdmin):
    """
    Set User Admin to be inline
    """
    inlines = (ParkingUserInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
