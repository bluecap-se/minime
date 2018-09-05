import string
import random

from django.contrib.auth import hashers
from rest_framework import serializers

from . import models
from . import utils


class UrlSerializer(serializers.ModelSerializer):
    hash = serializers.SlugField(required=False)
    password = serializers.CharField(required=False, write_only=True)

    class Meta:
        model = models.Url
        fields = ('hash', 'url', 'password')

    def create(self, validated_data):
        """
        Overrides super method.

        :param data: Data object
        :return: DB instance
        """
        validated_data['hash'] = self.create_hash()

        if validated_data.get('password', None):
            validated_data['password'] = hashers.make_password(validated_data['password'])

        instance = super(UrlSerializer, self).create(validated_data)

        if instance:
            utils.cache_set_url(instance.hash, instance.url)
            utils.cache_set_hash_taken(instance.hash)

        return instance

    def compare_passwords(self, against):
        return hashers.check_password(against, self.instance.password)

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
