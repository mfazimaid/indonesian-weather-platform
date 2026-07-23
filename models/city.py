"""
============================================================
Model: City

Description;
    Domain model representing a city from weather.dim_city.

author: Muhammad Fauzan Azima
============================================================
"""

from dataclasses import dataclass


@dataclass(slots=True)
class City:
    """
    Represents one city stored in the warehouse.
    """

    city_id: int
    city_name: str
    province: str
    latitude: float
    longitude: float
    timezone: str
