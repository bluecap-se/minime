import requests
from django.core.cache import cache
from django.http import request
from typing import Union
from minime import models


def cache_set_url(hash: str, url: str) -> str:
    return cache.set("short:url:{}".format(hash), url, 60 * 60 * 24 * 7)


def cache_get_short_url(hash: str) -> str:
    return cache.get("short:url:{}".format(hash))


def cache_set_hash_taken(hash: str) -> str:
    return cache.set("hash:taken:{}".format(hash), 1, None)


def cache_is_hash_taken(hash: str) -> bool:
    return cache.get("hash:taken:{}".format(hash)) is not None


def create_stats(request: request, hash: str) -> Union[models.Visitors, None]:
    """
    Creates stats for redirection hash

    TODO: Run this function async with Celery

    :param request: Request object
    :param hash: Redirect hash
    :return: Created `Visitor` db object
    """
    urlobj = models.Url.objects.filter(hash=hash).first()

    if not urlobj:
        return

    if request.user_agent.is_mobile:
        platform = "mobile"
    elif request.user_agent.is_tablet:
        platform = "tablet"
    elif request.user_agent.is_pc:
        platform = "desktop"
    elif request.user_agent.is_bot:
        platform = "bot"
    else:
        platform = "other"

    visitor_obj = models.Visitors(
        url=urlobj,
        browser_family=request.user_agent.browser.family,
        browser_version=request.user_agent.browser.version_string,
        os_family=request.user_agent.os.family,
        os_version=request.user_agent.os.version_string,
        device=request.user_agent.device.family,
        platform=platform,
        is_mobile=request.user_agent.is_mobile or request.user_agent.is_tablet,
    )

    visitor_obj.save()

    return visitor_obj


def get_current_app_version(use_cache: bool = True) -> dict:
    cache_key = "react_version"
    if use_cache:
        in_cache = cache.get(cache_key)
        if in_cache:
            return in_cache

    cdn_url = "http://minime-static-frontend.s3-website-eu-west-1.amazonaws.com/app/master/CURRENT_VERSION"
    data = requests.get(cdn_url).json()
    cache.set(cache_key, data, timeout=86400000)
    return data


def build_react_urls(data: dict) -> list:
    urls = data.get("files", [])
    version = data.get("version")

    return [
        f"http://minime-static-frontend.s3-website-eu-west-1.amazonaws.com/app/master/{version}/{u}"
        for u in urls
    ]
