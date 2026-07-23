from clients.weather_client import WeatherClient
from etl.extract.extract_weather import WeatherExtractor
from etl.load.load_weather import WeatherLoader
from etl.transform.transform_weather import WeatherTransformer
from etl.utils.report import PipelineReport
from pipeline import WeatherPipeline
from repositories.city_repository import CityRepository
from repositories.date_repository import DateRepository


def create_pipeline():

    report = PipelineReport()

    city_repository = CityRepository()
    date_repository = DateRepository()

    weather_client = WeatherClient()

    extractor = WeatherExtractor(
        report=report,
        city_repository=city_repository,
        weather_client=weather_client,
    )

    transformer = WeatherTransformer(
        report=report,
    )

    loader = WeatherLoader(
        report=report,
        city_repository=city_repository,
        date_repository=date_repository,
    )

    return WeatherPipeline(
        report=report,
        extractor=extractor,
        transformer=transformer,
        loader=loader,
    )
