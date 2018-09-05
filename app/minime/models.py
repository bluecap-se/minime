from django.db import models


class Url(models.Model):
    hash = models.SlugField(max_length=6)
    url = models.URLField(max_length=2048)
    created = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=1024, null=True)

    class Meta:
        indexes = [
            models.Index(fields=['hash'])
        ]


class Visitors(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    browser_family = models.CharField(max_length=100)
    browser_version = models.CharField(max_length=100)
    os_family = models.CharField(max_length=100)
    os_version = models.CharField(max_length=100)
    device = models.CharField(max_length=100)
    platform = models.CharField(max_length=100)
    is_mobile = models.BooleanField()
