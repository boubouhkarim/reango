from .base import *

SECRET_KEY = 'ojk@86z9*$zyuhge#3)p*%$q0psoo2lq*tv9jw90#1eezcl^y2'

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(SRC_DIR, 'db.sqlite3'),
    }
}