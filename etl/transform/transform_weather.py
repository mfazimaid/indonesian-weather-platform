import json
import os
from datetime import datetime

import pandas as pd

from utils.logger import logger


class WeatherTransformer:
    def __init__(self, report, process_date=None):
        self.report = report

        if process_date is None:
            process_date = datetime.now().strftime("%Y-%m-%d")

        self.process_date = process_date
        self.raw_path = os.path.join("data", "raw", self.process_date)

        self.processed_path = os.path.join("data", "processed", self.process_date)

        os.makedirs(self.processed_path, exist_ok=True)

    def get_json_files(self):
        logger.info(f"mencari file pada {self.raw_path}")

        return [file for file in os.listdir(self.raw_path) if file.endswith(".json")]

    def read_json(self, filename):
        filepath = os.path.join(self.raw_path, filename)

        logger.info(f"membaca {filename}")

        with open(filepath) as file:
            data = json.load(file)
        return data

    def parse_weather(self, city_name, data):
        current = data["current"]

        return {
            "city_name": city_name,
            "datetime": current["time"],
            "temperature": current["temperature_2m"],
            "humidity": current["relative_humidity_2m"],
            "wind_speed": current["wind_speed_10m"],
            "wind_direction": current["wind_direction_10m"],
        }

    def transform_all(self):
        logger.info("memulai proses transformasi.")

        records = []
        files = self.get_json_files()

        for file in files:
            logger.info(f"transformasi {file}")
            data = self.read_json(file)
            city = file.replace(".json", "")

            weather = self.parse_weather(city, data)
            records.append(weather)

        logger.info(f"{len(records)} record berhasil dibuat.")
        return records

    def create_dataframe(self, records):
        logger.info("membuat dataframe...")

        df = pd.DataFrame(records)

        self.report.add("Transform Rows", len(df))

        logger.info(f"{len(df)} baris berhasil dibuat.")
        return df

    def save_csv(self, dataframe):
        filename = os.path.join(self.processed_path, "weather.csv")

        dataframe.to_csv(filename, index=False)

        logger.info(f"CSV berjasil disimpan: {filename}")

    def run(self):

        logger.info("=" * 60)
        logger.info("Weather Transform Start")
        logger.info(f"Pprocess date: {self.process_date}")
        logger.info("=" * 60)

        records = self.transform_all()
        dataframe = self.create_dataframe(records)

        self.save_csv(dataframe)

        logger.info("=" * 60)
        logger.info("Weather Transform Finished")
        logger.info("=" * 60)


# if __name__ == "__main__":
# 	transformer = WeatherTransformer()
# 	records = transformer.transform_all()
# 	df = transformer.create_dataframe(records)
# 	transformer.save_csv(df)
# 	print(df)
