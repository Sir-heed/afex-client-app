from devtest.settings.base import *
from decouple import config
import dj_database_url

ALLOWED_HOSTS = ['afex-client-app.herokuapp.com']

# Hosing on heroku
import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)