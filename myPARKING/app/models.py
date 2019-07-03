"""
Definition of models.
"""
from django.contrib.auth.models import User
from django.db import models

from core.models import TimeStampedModel


class ParkingUser(TimeStampedModel):
    """
    This model extends from the Django internal user model
    to add user information
    """
    HONDA = 'hda'
    TOYOTA = 'tya'
    FORD = 'fd'
    JEEP = 'jp'
    OTHER = 'oth'
    CAR_TYPE_CHOICES = (
        (HONDA, 'Honda'),
        (TOYOTA, 'Toyota'),
        (FORD, 'Ford'),
        (JEEP, 'Jeep'),
        (OTHER, 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phonenumber = models.IntegerField('Phone Number', default=8675309)
    licenseplate = models.CharField('License Plate', max_length=10)
    cartype = models.CharField('Car Type', max_length=3,
                               choices=CAR_TYPE_CHOICES,
                               default=OTHER)

    def __str__(self):
        return '%s' % str(self.user)

    class Meta:
        verbose_name = 'Parking User'
        verbose_name_plural = 'Parking Users'
