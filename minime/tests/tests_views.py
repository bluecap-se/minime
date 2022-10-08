from django.core.cache import cache
from django.test import Client, TestCase, utils
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from minime import models


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    @utils.override_settings(DEBUG=True)
    def test_view_index(self):
        response = self.client.get(reverse("minime:home"))
        self.assertEqual(response.status_code, 200)


class ViewRedirectTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.hash = "abcABC"
        self.url = "http://127.0.0.1:8000/"
        self.url_obj = models.Url(url=self.url, hash=self.hash)
        self.url_obj.save()

    def test_fail_wrong_hash(self):
        hash = "abcdef"
        response = self.client.get(reverse("minime:redirect", kwargs=dict(hash=hash)))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_pass(self):
        self.assertEqual(models.Visitors.objects.filter(url=self.url_obj).count(), 0)
        self.assertIsNone(cache.get("short:url:{}".format(self.hash)))

        response = self.client.get(
            reverse("minime:redirect", kwargs=dict(hash=self.hash))
        )
        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(response.headers["location"], self.url)

        self.assertEqual(cache.get("short:url:{}".format(self.hash)), self.url)

        self.assertEqual(models.Visitors.objects.filter(url=self.url_obj).count(), 1)


class ViewShortenTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_fail_wrong_url_format(self):
        url = "not-a-url"
        response = self.client.post(reverse("minime:shorten"), {"url": url})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["url"][0], "Enter a valid URL.")
        self.assertEqual(models.Url.objects.count(), 0)

        response = self.client.post(
            reverse("minime:shorten"), {"url": url, "password": "abc"}
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["url"][0], "Enter a valid URL.")
        self.assertEqual(models.Url.objects.count(), 0)

    def test_pass_empty_password(self):
        url = "http://127.0.0.1:8000/"
        response = self.client.post(reverse("minime:shorten"), {"url": url})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["url"], url)
        self.assertEqual(models.Url.objects.count(), 1)
        self.assertIsNotNone(models.Url.objects.get(hash=response.data["hash"]))
        self.assertIsNone(models.Url.objects.get(hash=response.data["hash"]).password)

    def test_pass_with_password(self):
        url = "http://127.0.0.1:8000/"
        password = "abc"
        response = self.client.post(
            reverse("minime:shorten"), {"url": url, "password": password}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["url"], url)
        self.assertEqual(models.Url.objects.count(), 1)
        self.assertIsNotNone(models.Url.objects.get(hash=response.data["hash"]))
        self.assertIsNotNone(
            models.Url.objects.get(hash=response.data["hash"]).password
        )
