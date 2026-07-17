from abc import ABC, abstractmethod
from datetime import datetime

from app.core.logger import Logger


class BaseEngine(ABC):

    def __init__(self):

        self.started_at = None
        self.finished_at = None

    def before_run(self):

        self.started_at = datetime.now()

        Logger.info(
            f"{self.__class__.__name__} started"
        )

    @abstractmethod
    def process(self):
        pass

    def after_run(self):

        self.finished_at = datetime.now()

        duration = (
            self.finished_at - self.started_at
        ).total_seconds()

        Logger.info(
            f"{self.__class__.__name__} finished ({duration:.2f}s)"
        )

    def run(self):

        self.before_run()

        result = self.process()

        self.after_run()

        return result