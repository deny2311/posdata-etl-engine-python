from dataclasses import dataclass


@dataclass
class FTPConfig:

    name: str

    protocol: str

    host: str

    username: str

    password: str

    port: int = 21

    timeout: int = 30