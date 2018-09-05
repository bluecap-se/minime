from django.test import TestCase
from django.contrib.auth import hashers

from .. import models
from .. import serializers


class SerializerTestCase(TestCase):

    def test_fail_wrong_url(self):
        input_data = {
            'url': 'not-a-url',
        }

        serializer_instance = serializers.UrlSerializer(data=input_data)
        self.assertFalse(serializer_instance.is_valid())
        self.assertEqual(serializer_instance.errors, {'url': ['Enter a valid URL.']})

    def test_pass_empty_password(self):
        input_data = {
            'url': 'http://127.0.0.1:8000/',
        }

        serializer_instance = serializers.UrlSerializer(data=input_data)
        self.assertTrue(serializer_instance.is_valid(raise_exception=True))
        self.assertEqual(serializer_instance.errors, {})

        res = serializer_instance.save()
        self.assertEqual(res.url, input_data['url'])
        self.assertIsNotNone(res.hash)
        self.assertIsNone(res.password)

    def test_pass_with_password(self):
        input_data = {
            'url': 'http://127.0.0.1:8000/',
            'password': 'pass123'
        }

        serializer_instance = serializers.UrlSerializer(data=input_data)
        self.assertTrue(serializer_instance.is_valid(raise_exception=True))
        self.assertEqual(serializer_instance.errors, {})

        data = serializer_instance.validated_data
        self.assertEqual(data['url'], input_data['url'])

        res = serializer_instance.save()

        self.assertEqual(res.url, input_data['url'])
        self.assertIsNotNone(res.hash)
        self.assertIsNotNone(res.password)

    def test_pass_password_compare(self):
        input_data = {
            'url': 'http://127.0.0.1:8000/',
            'hash': 'abcdef',
            'password': 'pass123'
        }
        serializer_instance = serializers.UrlSerializer(data=input_data)
        serializer_instance.is_valid()
        serializer_instance.save()

        u = models.Url.objects.first()
        serializer_instance = serializers.UrlSerializer(u)

        self.assertFalse(serializer_instance.compare_passwords(''))
        self.assertTrue(serializer_instance.compare_passwords(input_data['password']))
