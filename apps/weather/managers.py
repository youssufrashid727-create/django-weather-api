from django.db import models
from django.utils import timezone
from datetime import timedelta


class WeatherCacheManager(models.Manager):
    def recent(self):
        return self.filter(
            cached_at__gte=timezone.now() - timedelta(minutes=30)
        )