import requests
from django.conf import settings
from .models import WeatherCache


class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

    def fetch_weather(self, location):
        params = {
            "lat": location.lat,
            "lon": location.lon,
            "appid": settings.OPENWEATHER_API_KEY,
            "units": "metric",
        }

        response = requests.get(self.BASE_URL, params=params)

        if response.status_code != 200:
            return None

        return response.json()

    def save_weather(self, location, data):
        return WeatherCache.objects.create(
            location=location,
            temperature=data["main"]["temp"],
            feels_like=data["main"]["feels_like"],
            humidity=data["main"]["humidity"],
            wind_speed=data["wind"]["speed"],
            description=data["weather"][0]["description"],
        )

    def get_weather(self, location):
        cached = WeatherCache.objects.filter(
            location=location
        ).order_by("-cached_at").first()

        if cached:
            return cached, True

        data = self.fetch_weather(location)

        if not data:
            raise Exception("OpenWeather API failed or invalid API key")

        weather = self.save_weather(location, data)

        return weather, False