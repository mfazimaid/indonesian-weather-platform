"""
============================================================
Client: Base Client

Description:
    Base HTTP Client

author: Muhammad Fauzan Azima
============================================================
"""

import time
from typing import Any, cast

import requests

from config.config import settings
from utils.logger import logger


class BaseClient:
    def get(self, url: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        """
        Execute HTTP GET request with retry mechanism.

        args:
            url:
                taget endpoint.

            params:
                query parameters.

        returns:
            JSON response.

        raises:
            RequestException
        """
        for attempt in range(settings.MAX_RETRY):
            logger.info("Attempt %s/%s", attempt + 1, settings.MAX_RETRY)

            try:
                response = requests.get(
                    url=url, params=params, timeout=settings.REQUEST_TIMEOUT
                )

                response.raise_for_status()

                return cast(dict[str, Any], response.json())

            except requests.RequestException as e:
                logger.warning("Attempt %s failed: %s", attempt + 1, e)

                if attempt == settings.MAX_RETRY - 1:
                    logger.error("Maximum retry reached.")

        raise RuntimeError("unexpected execution path")

        time.sleep(settings.RETRY_DELAY)
