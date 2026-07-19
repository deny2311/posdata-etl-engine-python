from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

from app.enums import JobStatus
from app.enums import TransferProtocol


@dataclass
class DownloadJob:
    """
    Domain model for downloader engine.
    """

    # ==========================================================
    # INPUT
    # ==========================================================

    store: str
    trx_date: datetime

    # ==========================================================
    # TRANSFER
    # ==========================================================

    transfer_name: Optional[str] = None
    protocol: Optional[TransferProtocol] = None

    # ==========================================================
    # REMOTE
    # ==========================================================

    remote_path: str = ""
    remote_filename: Optional[str] = None

    # ==========================================================
    # LOCAL
    # ==========================================================

    local_directory: Optional[Path] = None
    local_filename: Optional[str] = None

    # ==========================================================
    # PROCESS
    # ==========================================================

    retry: int = 0
    status: JobStatus = JobStatus.WAITING

    # ==========================================================
    # RUNTIME
    # ==========================================================

    started_at: Optional[datetime] = None
    finished_at: Optional[datetime] = None
    duration: float = 0.0

    error_message: Optional[str] = None

    # ==========================================================
    # META
    # ==========================================================

    created_at: datetime = field(default_factory=datetime.now)

    # ==========================================================
    # HELPER
    # ==========================================================

    @property
    def remote_file(self) -> str:

        if not self.remote_filename:
            return ""

        if self.remote_path:
            return f"{self.remote_path.rstrip('/')}/{self.remote_filename}"

        return self.remote_filename

    @property
    def local_file(self) -> Optional[Path]:

        if self.local_directory is None:
            return None

        if self.local_filename is None:
            return None

        return self.local_directory / self.local_filename

    @property
    def filename(self) -> str:

        return self.remote_filename or ""

    @property
    def is_finished(self) -> bool:

        return self.status in (
            JobStatus.SUCCESS,
            JobStatus.FAILED,
            JobStatus.CANCELLED,
        )

    def reset(self) -> None:

        self.retry = 0
        self.status = JobStatus.WAITING

        self.started_at = None
        self.finished_at = None

        self.duration = 0

        self.error_message = None