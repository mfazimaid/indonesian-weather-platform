import time

from utils.logger import logger


class WeatherPipeline:
    def __init__(
        self,
        report,
        extractor,
        transformer,
        loader,
    ):
        self.report = report
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self):
        start_time = time.time()

        try:
            self.extractor.run()
            self.transformer.run()
            self.loader.run()

            self.report.add(
                "status",
                "SUCCESS",
            )

        except Exception:
            logger.exception("pipeline failed...")

            self.report.add(
                "status",
                "FAILED",
            )

            raise

        finally:
            duration = round(
                time.time() - start_time,
                2,
            )

            self.report.add(
                "Duration",
                f"{duration} sec",
            )

            self.report.print()
