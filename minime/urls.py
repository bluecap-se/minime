from django.urls import path, re_path

from minime import views


app_name = "minime"

urlpatterns = [
    path("", views.index, name="home"),
    re_path(r"(?P<hash>\w{6})", views.redirect, name="redirect"),
    path("shorten/", views.CreateShortUrl.as_view(), name="shorten"),
]
