import tracemalloc
import sys
import logging
import sentry_sdk


class CustomFilter(logging.Filter):

    COLOR = {
        "DEBUG": "GREEN",
        "INFO": "GREEN",
        "WARNING": "YELLOW",
        "ERROR": "RED",
        "CRITICAL": "RED",
    }

    def filter(self, record):
        record.color = CustomFilter.COLOR[record.levelname]
        return True

def createLogger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler2 = logging.FileHandler(f"project.log", mode='w')
    formatter2 = logging.Formatter("%(name)s - %(levelname)s - %(asctime)s  : (%(filename)s).%(funcName)s(%(lineno)d) %(message)s",datefmt = '%Y-%m-%d %H:%M:%S')
    handler2.setFormatter(formatter2)
    logger.addHandler(handler2)
    logger.addFilter(CustomFilter())
    return logger
def createSentry(sentry_dsn: str):
    """
      :arg
      sentry_dsn - dsn for sentry project
      """
    sentry=sentry_sdk.init(
        dsn=sentry_dsn,
        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        traces_sample_rate=1.0,
        # Set profiles_sample_rate to 1.0 to profile 100%
        # of sampled transactions.
        # We recommend adjusting this value in production.
        profiles_sample_rate=1.0,
    )
    return sentry
