from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

from app.core import Storage
from app.enums import JobStatus, TransferProtocol


@dataclass
class DownloadJob:
    """
    ETL Pipeline Job

    One DownloadJob flows through the entire ETL process:

        Download
            ↓
        Extract
            ↓
        Import
            ↓
        Complete
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

    remote_path: str = ""
    remote_filename: Optional[str] = None

    # ==========================================================
    # LOCAL
    # ==========================================================

    local_filename: Optional[str] = None

    # ==========================================================
    # PIPELINE
    # ==========================================================

    extracted_files: list[Path] = field(default_factory=list)

    imported_files: list[Path] = field(default_factory=list)

    skipped_files: list[Path] = field(default_factory=list)

    warnings: list[str] = field(default_factory=list)

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

    created_at: datetime = field(
        default_factory=datetime.now
    )

    # ==========================================================
    # STORAGE
    # ==========================================================

    @property
    def download_directory(self) -> Path:

        return Storage().get("download")

    @property
    def extract_directory(self) -> Path:

        return (
            Storage().get("extract")
            /
            Path(self.local_filename).stem
        )

    # ==========================================================
    # FILE
    # ==========================================================

    @property
    def remote_file(self) -> str:

        if not self.remote_filename:
            return ""

        if self.remote_path:

            return (
                f"{self.remote_path.rstrip('/')}/"
                f"{self.remote_filename}"
            )

        return self.remote_filename

    @property
    def local_file(self) -> Optional[Path]:

        if not self.local_filename:

            return None

        return (
            self.download_directory
            /
            self.local_filename
        )

    @property
    def filename(self) -> str:

        return self.remote_filename or ""

    # ==========================================================
    # STATE
    # ==========================================================

    @property
    def is_finished(self) -> bool:

        return self.status in (

            JobStatus.SUCCESS,

            JobStatus.FAILED,

            JobStatus.CANCELLED

        )

    # ==========================================================
    # ACTION
    # ==========================================================

    def reset(self) -> None:

        self.retry = 0

        self.status = JobStatus.WAITING

        self.started_at = None

        self.finished_at = None

        self.duration = 0.0

        self.error_message = None

        self.extracted_files.clear()

        self.imported_files.clear()

        self.skipped_files.clear()

        self.warnings.clear()