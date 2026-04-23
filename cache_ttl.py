import time
from cache import cache_set, cache_get

def cache_set_with_ttl(key, value, ttl_seconds):
    cache_set(key, {"value": value, "expires": time.time() + ttl_seconds})

def cache_get_valid(key):
    entry = cache_get(key)
    if entry and entry["expires"] > time.time():
        return entry["value"]
    return None
