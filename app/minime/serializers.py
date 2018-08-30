import string
import random

from rest_framework import serializers
from django.core.cache import cache

from . import models

cache_tmpl = 'short:url:{}'
cache_ttl = 60 * 60 * 24 * 7  # 7 days


class UrlSerializer(serializers.ModelSerializer):
    hash = serializers.SlugField(required=False)

    class Meta:
        model = models.Url
        fields = ('hash', 'url')

    def create(self, data):
        """
        Overrides super method.

        :param data:
        :return:
        """
        data['hash'] = self.create_hash()

        instance = super(UrlSerializer, self).create(data)

        if instance:
            cache.set(cache_tmpl.format(instance.hash), instance.url, cache_ttl)
            cache.set('hash:taken:{}'.format(instance.hash), 1, None)

        return instance

    @staticmethod
    def create_hash():
        """
        Creates a unique hash

        TODO: Check hash in redis

        :return: Unique hash string
        """
        length = 6
        char = string.ascii_uppercase + string.digits + string.ascii_lowercase

        # Generate a new ID, until one is found that is unique
        while True:
            hash = ''.join(random.choice(char) for x in range(length))

            if not cache.get('hash:taken:{}'.format(hash)):
                return hash
