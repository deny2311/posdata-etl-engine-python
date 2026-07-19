from enum import Enum


class EngineState(str, Enum):
    IDLE = "IDLE"

    RUNNING = "RUNNING"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"