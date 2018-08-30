from django.core.cache import cache
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from rest_framework import generics

from . import forms
from . import models
from . import serializers


cache_tmpl = 'short:url:{}'
cache_ttl = 60 * 60 * 24 * 7  # 7 days


def index(request):
    return render(request, 'index.html', {'form': forms.ShortenURLForm})


def redirect(request, hash):

    url = cache.get(cache_tmpl.format(hash))

    if not url:
        urlobj = get_object_or_404(models.Url, hash=hash)  # gets object, if not found returns 404 error
        url = urlobj.url
        cache.set('short:url:{}'.format(hash), url, cache_ttl)

    return HttpResponseRedirect(url)


class CreateShortUrl(generics.CreateAPIView):
    queryset = models.Url.objects.all()
    serializer_class = serializers.UrlSerializer
