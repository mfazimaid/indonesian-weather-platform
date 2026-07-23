from repositories.city_repository import CityRepository


def test_get_all_city():
    repo = CityRepository()
    cities = repo.get_all()

    assert len(cities) == 10
    assert cities[0].city_name is not None
    assert cities[0].latitude is not None
    assert cities[0].longitude is not None


# RUNNING WITH: python3 -m pytest
