from pathlib import Path
from time import perf_counter

from app.core import Storage
from app.engines.base_engine import BaseEngine
from app.extractors import ExtractorFactory
from app.models import EngineResult


class ExtractorEngine(BaseEngine):

    def process(
        self,
        job
    ) -> EngineResult:

        started = perf_counter()

        storage = Storage()

        source = Path(job.local_file)

        if not source.exists():

            return EngineResult(

                success=False,

                message="Download file not found."

            )

        output = (
            storage.get("extract")
            /
            source.stem
        )

        extractor = ExtractorFactory.create()

        files = extractor.extract(
            source,
            output
        )

        return EngineResult(

            success=True,

            message=f"{len(files)} files extracted.",

            data=files,

            duration=perf_counter() - started

        )