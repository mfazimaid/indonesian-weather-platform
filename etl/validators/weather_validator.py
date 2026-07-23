import json
import os

from config.config import settings
from etl.utils.logger import logger


class WeatherValidator:
    def __init__(self, raw_path, report):

        self.raw_path = raw_path
        self.report = report
        self.weather_data = []

    def load_weather_files(self):

        files = os.listdir(self.raw_path)

        for file_name in files:
            file_path = os.path.join(self.raw_path, file_name)

            try:
                with open(file_path) as file:
                    data = json.load(file)

            except Exception:
                self.report.add("JSON Validation", "FAILED")

                raise Exception(f"{file_name} bukan JSON valid.")

            self.weather_data.append({"filename": file_name, "data": data})

        logger.info(
            "%s data berhasil dimuat.",
            len(self.weather_data),
        )

        self.report.add("JSON Validation", "PASS")

    def validate_total_file(self, expected):

        downloaded = len(self.weather_data)

        self.report.add("Expected File", expected)

        self.report.add("Downloaded File", downloaded)
        logger.info("%s file ditemukan.", downloaded)

        if downloaded != expected:
            self.report.add("File Validation", "FAILED")
            raise ValueError(f"Expected {expected}, tetapi hanya mendapat {downloaded}")

        self.report.add("File Validation", "PASS")

        logger.info("jumlah file valid.")

    def validate_empty_file(self):

        for weather in self.weather_data:
            filename = weather["filename"]
            data = weather["data"]

            if len(data) == 0:
                raise Exception(f"{filename} kosong.")

            self.report.add("Empty File", "PASS")

            logger.info("semua file memilikii isi.")

    def validate_schema(self):
        for weather in self.weather_data:
            filename = weather["filename"]
            data = weather["data"]

        current = data.get("current", {})

        required_fields = [
            "temperature_2m",
            "relative_humidity_2m",
            "wind_speed_10m",
            "wind_direction_10m",
        ]

        for field in required_fields:
            if field not in current:
                self.report.add("Schema Validation", "FAILED")

                raise Exception(f"{filename} kehilangan field{field}")
            self.report.add("Schema Validation", "PASS")

            logger.info("Schema Validation berhasil.")

    def validate_range(self, field, min_value, max_value, validation_name):
        logger.info(f"validasi {validation_name}...")

        for weather in self.weather_data:
            filename = weather["filename"]
            data = weather["data"]

            value = data["current"][field]

            if value < min_value or value > max_value:
                self.report.add(validation_name, "FAILED")

            raise Exception(f"{filename} {field} tidak valid: {value}")

    def validate_temperature(self):
        logger.info("validasi temperature...")

        for weather in self.weather_data:
            filename = weather["filename"]
            data = weather["data"]

            temperature = data["current"]["temperature_2m"]

            if (
                temperature < settings.MIN_TEMPERATURE
                or temperature > settings.MAX_TEMPERATURE
            ):
                self.report.add("Temperature Validation", "FAILED")

                raise Exception(f"{filename} temperature tidak valid: {temperature}")

        self.report.add("Temperature Validation", "PASS")
        logger.info("Temperature valid.")

    def validate_humidity(self):
        logger.info("validasi humidity...")

        for weather in self.weather_data:
            filename = weather["filename"]
            data = weather["data"]

            humidity = data["current"]["relative_humidity_2m"]

            if humidity < settings.MIN_HUMIDITY or humidity > settings.MAX_HUMIDITY:
                self.report.add("Humidity Validation", "FAILED")

                raise Exception(f"{filename} humidity tidak valid: {humidity}")

        self.report.add("Humidity Validation", "PASS")
        logger.info("Humidity valid.")

    def validate_wind_speed(self):
        logger.info("validasi wind speed...")

        for weather in self.weather_data:
            filename = weather["filename"]
            data = weather["data"]

            wind = data["current"]["wind_speed_10m"]

            if wind < settings.MIN_WIND_SPEED or wind > settings.MAX_WIND_SPEED:
                self.report.add("Wind Speed Validation", "FAILED")

                raise Exception(f"{filename} Wind Speed tidak valid: {wind}")

        self.report.add("Wind Speed Validation", "PASS")
        logger.info("Wind Speed valid.")

    def validate_wind_direction(self):
        logger.info("validasi wind direction...")

        for weather in self.weather_data:
            filename = weather["filename"]
            data = weather["data"]

        wind_direction = data["current"]["wind_direction_10m"]

        if (
            wind_direction < settings.MIN_WIND_DIRECTION
            or wind_direction > settings.MAX_WIND_DIRECTION
        ):
            self.report.add("Wind Direction Validation", "FAILED")

            raise Exception(
                f"{filename} Wind Directiion tidak valid: {wind_direction}."
            )

        self.report.add("Wind Direction Validation", "PASS")

        logger.info("Wind Direction valid.")

    def validate_duplicate(self):

        logger.info("validasi duplicate...")

        filenames = set()

        for weather in self.weather_data:
            filename = weather["filename"]

            if filename in filenames:
                self.report.add("duplicate validation", "FAILED")

                raise Exception(f"{filename} duplicate ditemukan.")

            filenames.add(filename)

        self.report.add("duplicate validation", "PASS")

        logger.info("duplicate tidak ditemukan.")

    def run(self, expected):

        logger.info("*" * 60)
        logger.info("Weather Validation Start")
        logger.info("*" * 60)

        self.load_weather_files()
        self.validate_total_file(expected)
        self.validate_empty_file()
        self.validate_schema()
        self.validate_temperature()
        self.validate_humidity()
        self.validate_duplicate()
        self.validate_wind_speed()
        self.validate_wind_direction()

        logger.info("semua validasi berhasil.")
        logger.info("*" * 60)
        logger.info("Weather Validation Finished.")
        logger.info("*" * 60)
