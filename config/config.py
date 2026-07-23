import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    # =============================================
    # 					DATABASE
    DB_HOST: str = os.getenv("DB_HOST", "localhost")
    DB_PORT: int = int(os.getenv("DB_PORT", 5432))
    DB_NAME: str = os.getenv("DB_NAME", "warehouse")
    DB_USER: str = os.getenv("DB_USER", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    # ==================================================

    API_BASE_URL: str = os.getenv(
        "API_BASE_URL", "https://api.open-meteo.com/v1/forecast"
    )

    REQUEST_TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", 30))

    MAX_RETRY: int = int(os.getenv("MAX_RETRY", 3))

    RETRY_DELAY: int = int(os.getenv("RETRY_DELAY", 2))

    RAW_FOLDER: str = os.getenv("RAW_FOLDER", "data/raw")

    PROCESSED_FOLDER: str = os.getenv("PROCESSED_FOLDER", "data/processed")

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    MIN_TEMPERATURE: float = float(os.getenv("MIN_TEMPERATURE", -50))

    MAX_TEMPERATURE: float = float(os.getenv("MAX_TEMPERATURE", 60))

    MIN_HUMIDITY: int = int(os.getenv("MIN_HUMIDITY", 0))

    MAX_HUMIDITY: int = int(os.getenv("MAX_HUMIDITY", 100))

    EXPECTED_TOTAL_CITY: int = int(os.getenv("EXPECTED_TOTAL_CITY", 10))

    MIN_WIND_SPEED: int = int(os.getenv("MIN_WIND_SPEED", 0))

    MAX_WIND_SPEED: int = int(os.getenv("MAX_WIND_SPEED", 300))

    MIN_WIND_DIRECTION: int = int(os.getenv("MIN_WIND_DIRECTION", 0))

    MAX_WIND_DIRECTION: int = int(os.getenv("MAX_WIND_DIRECTION", 360))


settings = Settings()
