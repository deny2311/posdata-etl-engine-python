from abc import ABC, abstractmethod
from pathlib import Path


class BaseExtractor(ABC):

    @abstractmethod
    def extract(
        self,
        source: Path,
        destination: Path
    ) -> list[Path]:
        pass