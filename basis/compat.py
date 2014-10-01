# -*- coding: utf-8 -*-
import django
from django.conf import settings

DJANGO16 = django.VERSION >= (1, 6)
DJANGO15 = django.VERSION >= (1, 5)

if DJANGO15:
    AUTH_USER_MODEL = settings.AUTH_USER_MODEL
else:
    AUTH_USER_MODEL = 'auth.User'


def get_user_model():
    if DJANGO15:
        from django.contrib.auth import get_user_model
        return get_user_model()
    else:
        from django.contrib.auth.models import User
        return User
