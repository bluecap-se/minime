import string
import random
from django.contrib.auth import hashers
from rest_framework import serializers
from minime import models, utils


class UrlSerializer(serializers.ModelSerializer):
    hash = serializers.SlugField(required=False)
    password = serializers.CharField(required=False, write_only=True, allow_blank=True)

    class Meta:
        model = models.Url
        fields = ("hash", "url", "password")

    def create(self, data: dict) -> models.Url:
        """
        Overrides super method.

        :param data: Data object
        :return: DB instance
        """
        data["hash"] = self.create_hash()

        if data.get("password", None):
            data["password"] = hashers.make_password(data["password"])

        instance = super(UrlSerializer, self).create(data)

        if instance:
            utils.cache_set_url(instance.hash, instance.url)
            utils.cache_set_hash_taken(instance.hash)

        return instance

    @staticmethod
    def create_hash() -> str:
        """
        Creates a unique hash

        :return: Unique hash string
        """
        length = 6
        char = string.ascii_uppercase + string.digits + string.ascii_lowercase

        # Generate a new ID, until one is found that is unique
        while True:
            hash = "".join(random.choice(char) for _ in range(length))

            if not utils.cache_is_hash_taken(hash):
                return hash
