from dataclasses import dataclass


@dataclass
class TransferConfig:

    name: str

    protocol: str

    host: str

    username: str

    password: str

    port: int

    timeout: int = 30

    passive: bool = True

    remote_path: str = ""

    local_path: str = ""