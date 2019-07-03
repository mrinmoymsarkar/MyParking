# pylint: skip-file
from .base import *

DEBUG = True

ALLOWED_HOSTS = (
    'localhost','127.0.0.1'
)

SLACK_CHANNEL = '#myparkingdev'

# Third Parties Applications
INSTALLED_APPS += (
    #'debug_toolbar',
)

EMAIL_HOST = 'your-email-host.net'
EMAIL_HOST_USER = 'admin@your-site.com'
EMAIL_HOST_PASSWORD = 'PASSWORD'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path.join(PROJECT_ROOT, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
