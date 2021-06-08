import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = 'cg47_8n$8(fwqmfkqi123+r!kli-f2+-lbp*&sue_dzc9j#1$&3'

DEBUG = False


ALLOWED_HOSTS = ['127.0.0.1', '']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_control',
        'USER': 'dj_admin',
        'PASSWORD': 'qwerty123',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '../main/static')
]
STATIC_ROOT = os.path.join(BASE_DIR, '../main/static')