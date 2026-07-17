from pathlib import Path
import logging
from datetime import datetime

from app.core.config import Config


class Logger:

    _logger = None

    @classmethod
    def get_logger(cls):

        if cls._logger:
            return cls._logger

        log_path = Path(Config.get("LOG_PATH"))

        log_path.mkdir(parents=True, exist_ok=True)

        logfile = log_path / f"etl_{datetime.now():%Y%m%d}.log"

        logger = logging.getLogger("POSDATA_ETL")

        logger.setLevel(logging.INFO)

        logger.handlers.clear()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )

        file_handler = logging.FileHandler(
            logfile,
            encoding="utf-8"
        )

        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        logger.addHandler(console_handler)

        cls._logger = logger

        return logger

    @classmethod
    def info(cls, msg):
        cls.get_logger().info(msg)

    @classmethod
    def warning(cls, msg):
        cls.get_logger().warning(msg)

    @classmethod
    def error(cls, msg):
        cls.get_logger().error(msg)

    @classmethod
    def debug(cls, msg):
        cls.get_logger().debug(msg)