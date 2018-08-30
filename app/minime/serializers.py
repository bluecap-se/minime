import string
import random

from rest_framework import serializers

from . import models
from . import utils


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
            utils.cache_set_url(instance.hash, instance.url)
            utils.cache_set_hash_taken(instance.hash)

        return instance

    @staticmethod
    def create_hash():
        """
        Creates a unique hash

        :return: Unique hash string
        """
        length = 6
        char = string.ascii_uppercase + string.digits + string.ascii_lowercase

        # Generate a new ID, until one is found that is unique
        while True:
            hash = ''.join(random.choice(char) for _ in range(length))

            if not utils.cache_is_hash_taken(hash):
                return hash
