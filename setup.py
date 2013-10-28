# -*- coding: utf8 -*-
import os
from setuptools import setup, find_packages

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

setup(
    name="django-basis",
    version='0.1.2',
    url='http://github.com/frecar/django-basis',
    author='Fredrik Nygård Carlsen',
    author_email='me@frecar.no',
    description='Simple reusable django app for basic model functionality',
    packages=find_packages(exclude='tests'),
    tests_require=[
        'django>=1.4',
    ],
    test_suite='runtests.runtests',
    include_package_data=True,
)
