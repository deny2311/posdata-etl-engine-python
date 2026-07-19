import time
from abc import ABC
from abc import abstractmethod
from datetime import datetime

from app.core.logger import Logger
from app.models.engine_result import EngineResult


class BaseEngine(ABC):

    def before_run(self, job):

        Logger.info(f"{self.__class__.__name__} started")

        job.started_at = datetime.now()

    def after_run(self, job):

        job.finished_at = datetime.now()

        job.duration = (
            job.finished_at - job.started_at
        ).total_seconds()

        Logger.info(
            f"{self.__class__.__name__} finished "
            f"({job.duration:.2f}s)"
        )

    @abstractmethod
    def process(self, job) -> EngineResult:
        pass

    def run(self, job):

        start = time.perf_counter()

        try:

            self.before_run(job)

            result = self.process(job)

            self.after_run(job)

            result.duration = (
                time.perf_counter() - start
            )

            return result

        except Exception as e:

            Logger.error(str(e))

            self.after_run(job)

            return EngineResult(
                success=False,
                message=str(e),
                error=e,
                data=job,
                duration=time.perf_counter() - start
            )