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
