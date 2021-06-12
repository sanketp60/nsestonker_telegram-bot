import os
import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# example) SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': '5432',
    }
}

# example) MySQL
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': '',
#         'USER': '',
#         'PASSWORD': '',
#         'HOST': '',
#         'PORT': '',
#     }
# }

INSTALLED_APPS = (
    'data',
)

SECRET_KEY = env('SECRET_KEY')
