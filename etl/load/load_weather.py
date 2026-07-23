import os
from datetime import datetime

import pandas as pd

from etl.utils.database import get_connection
from utils.logger import logger


class WeatherLoader:
    def __init__(self, report, city_repository, date_repository, process_date=None):

        self.report = report
        self.city_repository = city_repository
        self.date_repository = date_repository

        if process_date is None:
            process_date = datetime.now().strftime("%Y-%m-%d")

        self.process_date = process_date

        self.csv_path = os.path.join(
            "data", "processed", self.process_date, "weather.csv"
        )

    def load_csv(self):

        logger.info("membaca CSV")

        df = pd.read_csv(self.csv_path)

        logger.info(f"{len(df)} data ditemukan.")
        return df

    def weather_exists(self, city_id, date_id):
        with get_connection() as conn:
            with conn.cursor() as cursor:
                cursor.execute(
                    """
					SELECT 1
					FROM weather.fact_weather
					WHERE city_id = %s
					and date_id = %s
					""",
                    (city_id, date_id),
                )
                result = cursor.fetchone()

        return result is not None

    def load_fact_weather(self):

        logger.info("memulai load fact weather...")

        df = self.load_csv()
        city_lookup = self.city_repository.get_lookup()
        date_lookup = self.date_repository.get_lookup()

        logger.info("%s data weather ditemukan.", len(df))

        conn = get_connection()
        cursor = conn.cursor()

        total_insert = 0

        for _, row in df.iterrows():
            # 1. parsing tanggal
            full_date = datetime.strptime(row.datetime.split("T")[0], "%Y-%m-%d").date()

            # 2. ambil ID dari lookup
            city_id = city_lookup[row.city_name]
            date_id = date_lookup[full_date]

            # 3. skip jika data sudah ada di database
            if self.weather_exists(city_id, date_id):
                logger.info(
                    "Weather already exists for city_id=%s date_id=%s. skip.",
                    city_id,
                    date_id,
                )
                continue

            # 4. insert data baru
            cursor.execute(
                """
					INSERT INTO weather.fact_weather
					(
						city_id,
						date_id,
						temperature,
						humidity,
						wind_speed,
						wind_direction
					)
					VALUES (%s,%s,%s,%s,%s,%s)
				""",
                (
                    city_id,
                    date_id,
                    row.temperature,
                    row.humidity,
                    row.wind_speed,
                    row.wind_direction,
                ),
            )
            total_insert += 1
        conn.commit()

        self.report.add("Inserted Rows", total_insert)
        cursor.close()
        conn.close()

        logger.info("%s data ditemukan.", len(df))

    def run(self):

        logger.info("=" * 60)
        logger.info("Weather Load Start")
        logger.info(f"process date: {self.process_date}")
        logger.info("=" * 60)

        self.load_fact_weather()

        logger.info("=" * 60)
        logger.info("Weather Load Finished")
        logger.info("=" * 60)
