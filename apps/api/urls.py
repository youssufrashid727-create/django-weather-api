from django.urls import path
from apps.api.views import (
    LocationListCreateAPIView,
    LocationDetailAPIView,
    WeatherAPIView,
    WeatherCacheListAPIView,
    WeatherLogListAPIView,
)

urlpatterns = [
    path("locations/", LocationListCreateAPIView.as_view()),
    path("locations/<int:pk>/", LocationDetailAPIView.as_view()),
    path("weather/<int:location_id>/", WeatherAPIView.as_view()),
    path("weather-cache/", WeatherCacheListAPIView.as_view()),
    path("weather-logs/", WeatherLogListAPIView.as_view()),
]