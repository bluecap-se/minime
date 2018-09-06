from django.shortcuts import get_object_or_404
from rest_framework import authentication

from . import models
from . import serializers


class CSRFAuth(authentication.SessionAuthentication):

    def authenticate(self, request):
        self.enforce_csrf(request)
        return True, None


class AdminAuth(authentication.SessionAuthentication):

    def authenticate(self, request, *args):

        self.enforce_csrf(request)

        hash = request.POST.get('hash', None)
        password = request.POST.get('password', None)

        instance = get_object_or_404(models.Url, hash=hash)
        serializer = serializers.UrlSerializer(instance)

        if not serializer.compare_passwords(password):
            return False, None

        return instance, None
