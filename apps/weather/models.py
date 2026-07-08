from django.conf import settings
from django.db import models
from .managers import WeatherCacheManager


class Location(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="locations"
    )
    city_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lat = models.FloatField()
    lon = models.FloatField()
    is_home = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.city_name}, {self.country}"


class WeatherCache(models.Model):
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="weather_cache"
    )
    temperature = models.FloatField()
    feels_like = models.FloatField()
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    description = models.CharField(max_length=200)
    cached_at = models.DateTimeField(auto_now=True)


class WeatherLog(models.Model):
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="weather_logs"
    )
    date = models.DateField()
    min_temp = models.FloatField()
    max_temp = models.FloatField()

    def __str__(self):
        return f"{self.location.city_name} - {self.date}"