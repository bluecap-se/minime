import string
import random

from . import models


def get_hash():
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
        try:
            models.Url.objects.get(hash=hash)
        except:
            return hash
