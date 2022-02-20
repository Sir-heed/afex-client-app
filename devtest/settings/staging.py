from devtest.settings.base import *
from decouple import config
import dj_database_url

ALLOWED_HOSTS = ['afex-client-app.herokuapp.com']

# Hosing on heroku
DATABASES = {
    "default": dj_database_url.config(default=config("DATABASE_URL"))
    }