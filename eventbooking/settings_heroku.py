"""
Heroku uses this settings file.
Was configured via:
  heroku config:set DJANGO_SETTINGS_MODULE=eventbooking.settings_heroku
"""

from settings_base import *

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

DEBUG = False

TEMPLATE_DEBUG = False

# Allow all host headers
ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'eventbooking.wsgi_heroku.application'

# Static asset configuration
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)