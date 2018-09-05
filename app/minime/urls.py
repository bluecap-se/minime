from django.conf.urls import url

from . import views


app_name = 'minime'

urlpatterns = [
    url(r'^$', views.view_index, name='home'),
    url(r'^r/(?P<hash>\w{6})$', views.view_redirect, name='redirect'),
    url(r'^shorten/$', views.CreateShortUrl.as_view(), name='shorten'),

    url(r'^r/(?P<hash>\w{6})\+$', views.view_admin_login, name='admin-login'),
    url(r'^dashboard/$', views.AdminDashboard.as_view(), name='admin-dashboard'),
]
