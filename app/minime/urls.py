from django.conf.urls import url

from . import views

app_name = 'minime'
urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^r/(?P<short_id>\w{6})$', views.redirect, name='redirect'),
    url(r'^shorten/$', views.shorten_url, name='shorten'),
]
