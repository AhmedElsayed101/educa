from .base import *

DEBUG = False

SECRET_KEY = 'secret'

ADMINS = (
    ('Ahmed', 'ahmedelee@gmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'educa',
        'USER': 'educa',
        'PASSWORD': 'educa', # should use env vars.
    }
}