from dataclasses import dataclass


@dataclass
class EngineResult:

    success: bool

    message: str = ""

    data: object = None