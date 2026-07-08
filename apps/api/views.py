from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.weather.models import Location, WeatherCache, WeatherLog
from apps.api.serializers import (
    LocationSerializer,
    WeatherCacheSerializer,
    WeatherLogSerializer,
)
from apps.weather.services import WeatherService


class LocationListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LocationDetailAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = LocationSerializer

    def get_queryset(self):
        return Location.objects.filter(user=self.request.user)


class WeatherAPIView(APIView):
    def get(self, request, location_id):
        location = get_object_or_404(
            Location,
            id=location_id,
            user=request.user,
        )

        service = WeatherService()
        weather, from_cache = service.get_weather(location)

        return Response({
            "location": str(location),
            "temperature": weather.temperature,
            "feels_like": weather.feels_like,
            "humidity": weather.humidity,
            "wind_speed": weather.wind_speed,
            "description": weather.description,
            "cached": from_cache,
        })


class WeatherCacheListAPIView(generics.ListAPIView):
    serializer_class = WeatherCacheSerializer

    def get_queryset(self):
        return WeatherCache.objects.filter(location__user=self.request.user)


class WeatherLogListAPIView(generics.ListAPIView):
    serializer_class = WeatherLogSerializer

    def get_queryset(self):
        return WeatherLog.objects.filter(location__user=self.request.user)