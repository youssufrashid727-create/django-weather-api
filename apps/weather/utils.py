from datetime import timedelta
from django.utils import timezone


def get_cached_weather(location):
    return location.weather_cache.order_by("-cached_at").first()


def is_cache_valid(cache):
    if not cache:
        return False

    return cache.cached_at >= timezone.now() - timedelta(minutes=30)