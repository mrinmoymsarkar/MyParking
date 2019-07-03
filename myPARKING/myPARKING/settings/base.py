# pylint: skip-file
"""
Django settings for myPARKING project.
"""

from os import path
PROJECT_ROOT = path.dirname(path.abspath(path.join(path.dirname(__file__), '..')))

ADMINS = (
    ('SUPER', 'superuser@admin.net'),
)

MANAGERS = ADMINS

LOGIN_URL = '/login/'
TIME_ZONE = 'America/Los_Angeles'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    path.join(PROJECT_ROOT, 'static').replace('\\', '/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'YOUR SECRET KEY'

SLACK_USERNAME = 'PS Parking'
SLACK_TOKEN = 'YOUR SLACK TOKEN'
SLACK_ENDPOINT_URL = 'https://hooks.slack.com/services/SOMEENDPOINT'
SLACK_BACKEND = 'django_slack.backends.UrllibBackend'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            path.join(PROJECT_ROOT, 'templates').replace('\\', '/'),
        ],
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]

MIDDLEWARE=[
    #'debug_toolbar.middleware.DebugToolbarMiddleware'
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTHENTICATION_BACKENDS = (
('django.contrib.auth.backends.ModelBackend'),
    # ... your other backends
    'app.auth_backends.EmailOrUsernameModelBackend',
)

ROOT_URLCONF = 'myPARKING.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'myPARKING.wsgi.application'

INSTALLED_APPS = (
    #'debug_toolbar',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

)

# Third party app
INSTALLED_APPS += (
    'django_cron',
    'django_slack',
)

# Internal Apps
INSTALLED_APPS += (
    'car',
    'app',
)

CRON_CLASSES = [
    "util.cron.CronJob"
]

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Specify the default test runner.
TEST_RUNNER = 'django.test.runner.DiscoverRunner'
