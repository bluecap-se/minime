from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from rest_framework import generics

from . import forms
from . import models
from . import serializers
from . import utils


def index(request):
    return render(request, 'index.html', {'form': forms.ShortenURLForm})


def redirect(request, hash):

    url = utils.cache_get_short_url(hash)

    if not url:
        urlobj = get_object_or_404(models.Url, hash=hash)  # gets object, if not found returns 404 error
        url = urlobj.url
        utils.cache_set_url(hash, url)

    return HttpResponseRedirect(url)


class CreateShortUrl(generics.CreateAPIView):
    queryset = models.Url.objects.all()
    serializer_class = serializers.UrlSerializer
