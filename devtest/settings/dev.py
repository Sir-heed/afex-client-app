from devtest.settings.base import *
from decouple import config

secret_key = config('SECRET_KEY')
debug = config('DEBUG', default=False, cast=bool)
db_name = config('DB_NAME')
db_user = config('DB_USER')
db_password = config('DB_PASSWORD')
db_port = config('DB_PORT')
db_host = config('DB_HOST')

DEBUG = debug
SECRET_KEY = secret_key

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': db_port,
    }
}