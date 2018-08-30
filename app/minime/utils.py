from django.core.cache import cache


cache_ttl = 60 * 60 * 24 * 7  # 7 days


def cache_set_url(hash, url):
    return cache.set('short:url:{}'.format(hash), url, cache_ttl)


def cache_get_short_url(hash):
    return cache.get('short:url:{}'.format(hash))


def cache_set_hash_taken(hash):
    return cache.set('hash:taken:{}'.format(hash), 1, None)


def cache_is_hash_taken(hash):
    return cache.get('hash:taken:{}'.format(hash)) is not None
