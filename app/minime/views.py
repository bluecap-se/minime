from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import generics

from . import forms
from . import models
from . import serializers
from . import utils


def view_index(request):
    """
    View to show home page

    :param request: Request object
    :return: Template http response
    """
    return render(request, 'index.html', {'form': forms.ShortenURLForm})


def view_redirect(request, hash):
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
        url = urlobj.url
        utils.cache_set_url(hash, url)

    utils.create_stats(request, hash)

    return HttpResponseRedirect(url)


class CreateShortUrl(generics.CreateAPIView):
    """
    View that saves url

    DRF POST view
    """
    queryset = models.Url.objects.all()
    serializer_class = serializers.UrlSerializer


"""

ADMIN VIEWS

"""


def view_admin_login(request, hash):
    """
    View to show admin login page

    :param request: Request object
    :param hash: Slug
    :return: Template http response
    """
    context = {
        'form': forms.AdminForm(initial={'hash': hash}),
        'message': request.session.get('form_message', None),
    }
    if request.session.get('form_message', None):
        del request.session['form_message']

    return render(request, 'admin/login.html', context)


class AdminDashboard(generics.CreateAPIView):
    """
    View that displays admin dashboard

    DRF POST view
    """
    queryset = models.Url.objects.all()
    serializer_class = serializers.UrlSerializer

    def post(self, request, *args, **kwargs):
        """
        TODO: Move to auth class
        :return:
        """
        hash = request.POST.get('hash', None)
        password = request.POST.get('password', None)

        instance = get_object_or_404(self.queryset, hash=hash)
        serializer = self.get_serializer(instance)

        if not serializer.compare_passwords(password):
            request.session['form_message'] = 'Wrong password, try again.'
            return redirect('minime:admin-login', hash=hash)

        """
        END MOVE
        """

        return render(request, 'admin/dashboard.html')
