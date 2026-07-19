from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional


@dataclass
class EngineResult:
    """
    Standard result returned by every Engine.
    """

    # ==========================================================
    # RESULT
    # ==========================================================

    success: bool

    message: str = ""

    # ==========================================================
    # DATA
    # ==========================================================

    data: Any = None

    files: list[Path] = field(default_factory=list)

    # ==========================================================
    # ERROR
    # ==========================================================

    error: Optional[Exception] = None

    warnings: list[str] = field(default_factory=list)

    # ==========================================================
    # PERFORMANCE
    # ==========================================================

    duration: float = 0.0

    # ==========================================================
    # HELPER
    # ==========================================================

    @property
    def has_warning(self) -> bool:

        return len(self.warnings) > 0

    @property
    def total_files(self) -> int:

        return len(self.files)

    def add_warning(
        self,
        message: str
    ) -> None:

        self.warnings.append(message)

    def add_file(
        self,
        file: Path
    ) -> None:

        self.files.append(file)