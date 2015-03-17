# -*- coding: utf8 -*-
import os
from setuptools import setup, find_packages

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'


def _read_long_description():
    try:
        import pypandoc
        return pypandoc.convert('README.md', 'rst', format='markdown')
    except Exception:
        return None


setup(
    name="django-basis",
    version='0.3.5',
    url='http://github.com/frecar/django-basis',
    author='Fredrik Carlsen',
    author_email='fredrik@carlsen.io',
    description='Simple reusable django app for basic model functionality',
    long_description=_read_long_description(),
    packages=find_packages(exclude='tests'),
    tests_require=[
        'django>=1.4',
    ],
    license='MIT',
    test_suite='runtests.runtests',
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ]
)
