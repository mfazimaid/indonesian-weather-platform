"""
============================================================
Client: Weather Client

Description:
    Client responsible for communicating with Open-Meteo API.
    HTTP Client for Open-Meteo API.

author: Muhammad Fauzan Azima
============================================================
"""

from typing import Any

from clients.base_client import BaseClient
from config.config import settings


class WeatherClient(BaseClient):
    def get_current_weather(self, latitude: float, longitude: float) -> dict[str, Any]:
        """
        Retrieve current weather data from Open-Meteo.

        Args:
            params:
                Query parameters.

        Returns:
            Weather response as JSON.
        """
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": ",".join(
                [
                    "temperature_2m",
                    "relative_humidity_2m",
                    "wind_speed_10m",
                    "wind_direction_10m",
                ]
            ),
        }

        return self.get(url=settings.API_BASE_URL, params=params)
