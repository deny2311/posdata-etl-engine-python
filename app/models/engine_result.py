from dataclasses import dataclass
from typing import Any
from typing import Optional


@dataclass
class EngineResult:

    success: bool

    message: str = ""

    data: Any = None

    error: Optional[Exception] = None

    duration: float = 0