# -*- coding: utf8 -*-
from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
                       url(r'^logs/', include('memento.urls')),
)