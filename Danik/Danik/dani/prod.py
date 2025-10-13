# Project Modules
from Danik.base import *


DEBUG = False
ALLOWED_HOSTS = [*]

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}