from etl.utils.logger import logger


class PipelineReport:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data[key] = value

    def get(self):
        return self.data

    def print(self):
        logger.info("=" * 60)
        logger.info("Pipeline Report")

        for key, value in self.data.items():
            logger.info(f"{key}: {value}")

        logger.info("=" * 60)
