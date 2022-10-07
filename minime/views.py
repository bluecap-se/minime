from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from minime import forms, models, serializers, utils


def index(request):
    """
    View to show home page

    :param request: Request object
    :return: Template http response
    """
    return render(
        request, "index.html", {"debug": settings.DEBUG, "form": forms.ShortenURLForm}
    )


def redirect(request, hash):
    """
    View that redirects to `Url.url` if it exists.
    Checks in Redis cache first.

    :param request: Request object
    :param hash: Slug
    :return: 404 or 301 http response
    """
    url = utils.cache_get_short_url(hash)

    if not url:
        urlobj = get_object_or_404(models.Url, hash=hash)
        url = getattr(urlobj, "url")
        utils.cache_set_url(hash, url)

    utils.create_stats(request, hash)

    return HttpResponseRedirect(url)


def ping(request):
    return HttpResponse(status=200)


class CreateShortUrl(generics.CreateAPIView):
    """
    View that saves url

    DRF POST view
    """

    queryset = models.Url.objects.all()
    serializer_class = serializers.UrlSerializer
