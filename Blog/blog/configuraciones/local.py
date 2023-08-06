from .settings import *

#DEBUG = True

#ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Soy_Burrodb',
        'USER': 'root',
        'PASSWORD': '@100xCienTo571318',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}