from .settings import *
from .settings import BASE_DIR
import os

ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

DEBUG = False

'''
CONNECTION = os.environ['AZURE']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydatabase",
        "HOST": "127.0.0.1",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
    }
}
'''