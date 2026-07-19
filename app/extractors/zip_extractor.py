from pathlib import Path
from zipfile import ZipFile

from .base_extractor import BaseExtractor


class ZipExtractor(BaseExtractor):

    def extract(
        self,
        source: Path,
        destination: Path
    ) -> list[Path]:

        destination.mkdir(
            parents=True,
            exist_ok=True
        )

        files = []

        with ZipFile(source, "r") as zip_file:

            zip_file.extractall(destination)

            for name in zip_file.namelist():

                files.append(
                    destination / name
                )

        return files