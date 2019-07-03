# pylint: skip-file
from .base import *

ALLOWED_HOSTS = (
    '.azurewebsites.net',
)

SLACK_CHANNEL = '#myparking'

EMAIL_HOST = 'your-email-host.net'
EMAIL_HOST_USER = 'admin@your-site.com'
EMAIL_HOST_PASSWORD = 'PASSWORD'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myparking-production',
        'USER': 'USERNAME',
        'PASSWORD': 'PASSWORD',
        'HOST': 'HOSTNAME',
        'PORT': '3306',
    }
}