import json

from django.core.cache import cache
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from . import forms
from . import models
from . import utils


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


def shorten_url(request):

    url = request.POST.get('url', '')

    if url:
        hash = utils.get_hash()
        b = models.Url(url=url, hash=hash)
        b.save()

        cache.set(cache_tmpl.format(hash), url, cache_ttl)
        cache.set('hash:taken:{}'.format(hash), 1, None)

        response_data = dict(url='{}/{}'.format(settings.SITE_URL, hash))
        return HttpResponse(json.dumps(response_data), content_type='application/json')

    return HttpResponse(json.dumps({'error': 'error occurs'}), content_type='application/json')
