# -*- coding: utf-8 -*-

from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', 'index', name='home'),
    url(r'^(?P<short_id>\w{4})$', 'redirectOriginal', name='redirectOriginal'),
    url(r'^makeshort/$', 'shortenUrl', name='shortenUrl'),
]
