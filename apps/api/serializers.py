from rest_framework import serializers
from apps.weather.models import Location, WeatherCache, WeatherLog


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"
        read_only_fields = ["user"]


class WeatherCacheSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherCache
        fields = "__all__"


class WeatherLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherLog
        fields = "__all__"