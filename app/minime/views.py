
import json
import random
import string

from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .forms import ShortenURLForm
from .models import Url


def index(request):
    return render(request, 'index.html', {'form': ShortenURLForm})


def redirect(request, short_id):
    url = get_object_or_404(Url, pk=short_id)  # gets object, if not found returns 404 error
    url.count += 1
    url.save()

    return HttpResponseRedirect(url.httpurl)


def shorten_url(request):

    url = request.POST.get('url', '')

    if url:
        short_id = get_short_code()
        b = Url(httpurl=url, short_id=short_id)
        b.save()

        response_data = dict(url='{}/{}'.format(settings.SITE_URL, short_id))
        return HttpResponse(json.dumps(response_data), content_type='application/json')

    return HttpResponse(json.dumps({'error': 'error occurs'}), content_type='application/json')


def get_short_code():
    length = 6
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase

    # Generate a new ID, until one is found that is unique
    while True:
        short_id = ''.join(random.choice(char) for x in range(length))
        try:
            Url.objects.get(pk=short_id)
        except:
            return short_id
