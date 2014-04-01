# -*- coding: utf-8 -*-
import django
from django.conf import settings

if django.VERSION >= (1, 5):
    AUTH_USER_MODEL = settings.AUTH_USER_MODEL
else:
    AUTH_USER_MODEL = 'auth.User'


def get_user_model():
    if django.VERSION >= (1, 5):
        from django.contrib.auth import get_user_model
        return get_user_model()
    else:
        from django.contrib.auth.models import User
        return User


def get_username(user):
    try:
        return user.get_username()
    except AttributeError:
        return user.username
