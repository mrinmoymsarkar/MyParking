"""
Definition of models.
"""
from django.db import models

from core.models import TimeStampedModel

from app.models import ParkingUser

class Car(TimeStampedModel):
    """
    This model extends from the Django internal user model
    to add user information
    """
    make = models.CharField('Auto Maker', max_length=50, unique=True)
    owners = models.ManyToManyField(ParkingUser,
                                    through='Vehicles',
                                    through_fields=('car', 'parking_user'))

    def __str__(self):
        return '%s' % (self.make)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

class Vehicles(TimeStampedModel):
    """
    Link users with vehicles
    """
    ALABAMA = 'AL'
    ALASKA = 'AK'
    ARIZONA = 'AZ'
    ARKANSAS = 'AR'
    CALIFORNIA = 'CA'
    COLORADO = 'CO'
    CONNECTICUT = 'CT'
    DELAWARE = 'DE'
    FLORIDA = 'FL'
    GEORGIA = 'GU'
    HAWAII = 'HI'
    IDAHO = 'ID'
    ILLINOIS = 'IL'
    INDIANA = 'IN'
    IOWA = 'IA'
    KANSAS = 'KS'
    KENTUCKY = 'KY'
    LOUISIANA = 'LA'
    MAINE = 'ME'
    MARYLAND = 'MD'
    MASSACHUSETTS = 'MA'
    MICHIGAN = 'MI'
    MINNESOTA = 'MN'
    MISSISSIPPI = 'MS'
    MISSOURI = 'MO'
    MONTANA = 'MT'
    NEBRASKA = 'NE'
    NEVADA = 'NV'
    NEW_HAMPSHIRE = 'NH'
    NEW_JERSEY = 'NJ'
    NEW_MEXICO = 'NM'
    NEW_YORK = 'NY'
    NORTH_CAROLINA = 'NC'
    NORTH_DAKOTA = 'ND'
    OHIO = 'OH'
    OKLAHOMA = 'OK'
    OREGON = 'OR'
    PENNSYLVANIA = 'PA'
    RHODE_ISLAND = 'RI'
    SOUTH_CAROLINA = 'SC'
    SOUTH_DAKOTA = 'SD'
    TENNESSEE = 'TN'
    TEXAS = 'TX'
    UTAH = 'UT'
    VERMONT = 'VT'
    VIRGINIA = 'VI'
    WASHINGTON = 'WA'
    WEST_VIRGINIA = 'WV'
    WISCONSIN = 'WI'
    WYOMING = 'WY'
    LICENSE_STATE_CHOICES = (
        (ALABAMA, 'Alabama'),
        (ALASKA, 'Alaska'),
        (ARIZONA, 'Arizona'),
        (ARKANSAS, 'Arkansas'),
        (CALIFORNIA, 'California'),
        (COLORADO, 'Colorado'),
        (CONNECTICUT, 'Connecticut'),
        (DELAWARE, 'Delaware'),
        (FLORIDA, 'Florida'),
        (GEORGIA, 'Georgia'),
        (HAWAII, 'Hawaii'),
        (IDAHO, 'Idaho'),
        (ILLINOIS, 'Illinois'),
        (INDIANA, 'Indiana'),
        (IOWA, 'Iowa'),
        (KANSAS, 'Kansas'),
        (KENTUCKY, 'Kentucky'),
        (LOUISIANA, 'Louisiana'),
        (MAINE, 'Maine'),
        (MARYLAND, 'Maryland'),
        (MASSACHUSETTS, 'Massachusetts'),
        (MICHIGAN, 'Michigan'),
        (MINNESOTA, 'Minnesota'),
        (MISSISSIPPI, 'Mississippi'),
        (MISSOURI, 'Missouri'),
        (MONTANA, 'Montana'),
        (NEBRASKA, 'Nebraska'),
        (NEVADA, 'Nevada'),
        (NEW_HAMPSHIRE, 'New Hampshire'),
        (NEW_JERSEY, 'New Jersey'),
        (NEW_MEXICO, 'New Mexico'),
        (NEW_YORK, 'New York'),
        (NORTH_CAROLINA, 'North Carolina'),
        (NORTH_DAKOTA, 'North Dakota'),
        (OHIO, 'Ohio'),
        (OKLAHOMA, 'Oklahoma'),
        (OREGON, 'Oregon'),
        (PENNSYLVANIA, 'Pennsylvania'),
        (RHODE_ISLAND, 'Rhode Island'),
        (SOUTH_CAROLINA, 'South Carolina'),
        (SOUTH_DAKOTA, 'South Dakota'),
        (TENNESSEE, 'Tennessee'),
        (TEXAS, 'Texas'),
        (UTAH, 'Utah'),
        (VERMONT, 'Vermont'),
        (VIRGINIA, 'Virginia'),
        (WASHINGTON, 'Washington'),
        (WEST_VIRGINIA, 'West Virginia'),
        (WISCONSIN, 'Wisconsin'),
        (WYOMING, 'Wyoming'),
        )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    parking_user = models.ForeignKey(ParkingUser, on_delete=models.CASCADE)
    license_state = models.CharField('License State',
                                     max_length=2,
                                     choices=LICENSE_STATE_CHOICES,
                                     default=CALIFORNIA)
    license_plate = models.CharField('License Plate', max_length=10)

    def __str__(self):
        return '%s: %s-%s' % (self.parking_user, self.car, self.license_plate)

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'
