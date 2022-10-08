from django.urls import path, re_path
from minime import views


app_name = "minime"

urlpatterns = [
    path("", views.index, name="home"),
    path("ping/", views.ping, name="ping"),
    path("shorten/", views.CreateShortUrl.as_view(), name="shorten"),
    path("reset-react-cache/", views.ReactResetView.as_view(), name="cache"),
    re_path(r"(?P<hash>\w{6})", views.redirect, name="redirect"),
]
