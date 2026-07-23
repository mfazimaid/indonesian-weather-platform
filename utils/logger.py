import logging
import os
from logging.handlers import TimedRotatingFileHandler

LOG_DIR = "logs"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "weather.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        TimedRotatingFileHandler(
            filename=LOG_FILE,
            when="midnight",
            interval=1,
            backupCount=30,
            encoding="utf-8",
        ),
    ],
)

logger = logging.getLogger("weather_etl")
