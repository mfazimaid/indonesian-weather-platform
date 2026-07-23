import json
import time
from datetime import datetime
from pathlib import Path

from config.config import settings
from etl.validators.weather_validator import WeatherValidator
from utils.logger import logger


class WeatherExtractor:
    def __init__(self, report, city_repository, weather_client, process_date=None):
        self.report = report
        self.city_repository = city_repository
        self.weather_client = weather_client

        if process_date is None:
            process_date = datetime.now().strftime("%Y-%m-%d")

        self.process_date = process_date

        self.raw_path = Path(settings.RAW_FOLDER) / self.process_date

        self.raw_path.mkdir(parents=True, exist_ok=True)

    def download_all(self):
        cities = self.city_repository.get_all()
        logger.info("%s cities found.", len(cities))

        self.report.add("Downloaded City", len(cities))

        for city in cities:
            logger.info("Downloading weather for %s", city.city_name)

            data = self.weather_client.get_current_weather(
                latitude=city.latitude, longitude=city.longitude
            )

            filename = self.raw_path / f"{city.city_name}.json"

            with open(filename, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

            logger.info("saved raw file: %s", filename)

        files = list(self.raw_path.glob("*.json"))
        logger.info(f"{len(files)} file berhasil di download.")
        logger.info("Total cities = %s", len(cities))
        validator = WeatherValidator(self.raw_path, self.report)

        validator.run(expected=len(cities))

    def run(self):
        start_time = time.time()

        logger.info("=" * 60)
        logger.info("Weather Extraction Start")
        logger.info(f"process date: {self.process_date}")
        logger.info("=" * 60)

        self.download_all()

        duration = round(time.time() - start_time, 2)

        logger.info("Duration: %.2f seconds", duration)

        logger.info("=" * 60)
        logger.info("Weather Extraction Finished")
        logger.info("=" * 60)
