import os
from django.conf import settings

DEBUG = False
TEMPLATE_DEBUG = True
DATABASES = settings.DATABASES


#Parse database configuration from $DATABASE_URL
import dj_database_url 
DATABASES['default'] = dj_database_url.config()

#Honor the x-forworded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#Allow all host headers
ALLOWED_HOSTS = ['*']

BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "joins_a", "static"), ]
