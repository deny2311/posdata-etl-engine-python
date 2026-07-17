from dataclasses import dataclass
from datetime import date


@dataclass
class DownloadJob:

    store: str

    trx_date: date

    remote_file: str = ""

    local_file: str = ""

    ftp_name: str = ""

    retry: int = 0

    status: str = "WAITING"