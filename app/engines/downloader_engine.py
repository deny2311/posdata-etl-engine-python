from app.builders import FilenameBuilder

from app.core.logger import Logger
from app.core.storage import Storage

from app.engines.base_engine import BaseEngine

from app.enums import JobStatus

from app.models import DownloadJob
from app.models import EngineResult

from app.repositories import TransferRepository

from app.services.transfer import TransferFactory


class DownloaderEngine(BaseEngine):
    """
    Downloader Engine

    Workflow

    validate()

    prepare()

    connect()

    download()

    verify()

    cleanup()
    """

    def __init__(self):

        super().__init__()

        self.storage = Storage()

        self.storage.create()

        self.repository = TransferRepository()

        self.config = None

        self.service = None

    # ==========================================================

    def process(
        self,
        job: DownloadJob
    ) -> EngineResult:

        try:

            self.validate(job)

            self.prepare(job)

            self.connect(job)

            self.download(job)

            self.verify(job)

            job.status = JobStatus.SUCCESS

            return EngineResult(

                success=True,

                message="Download completed successfully.",

                data=job

            )

        except Exception as ex:

            job.status = JobStatus.FAILED

            job.error_message = str(ex)

            Logger.error(str(ex))

            return EngineResult(

                success=False,

                message=str(ex),

                error=ex,

                data=job

            )

        finally:

            self.cleanup(job)

    # ==========================================================

    def validate(
        self,
        job: DownloadJob
    ) -> None:

        Logger.info("Validate Download Job")

        if not job.store:

            raise ValueError(
                "Store is required."
            )

        if job.trx_date is None:

            raise ValueError(
                "Transaction date is required."
            )

    # ==========================================================

    def prepare(
        self,
        job: DownloadJob
    ) -> None:

        Logger.info("Prepare Download Job")

        #
        # Transfer Config
        #

        self.config = self.repository.get(
            job.store
        )

        job.transfer_name = self.config.name

        job.protocol = self.config.protocol

        job.remote_path = self.config.remote_path

        #
        # Filename
        #

        filename = FilenameBuilder.build_download_filename(
            job
        )

        job.remote_filename = filename

        job.local_filename = filename

        #
        # Local Folder
        #

        if job.local_directory is None:

            root = self.storage.get(
                "download"
            )

            job.local_directory = (
                root / job.store
            )

        job.local_directory.mkdir(

            parents=True,

            exist_ok=True

        )

    # ==========================================================

    def connect(
        self,
        job: DownloadJob
    ) -> None:

        Logger.info(
            f"Connect : {job.transfer_name}"
        )

        self.service = TransferFactory.create(
            self.config
        )

        self.service.connect()

        job.status = JobStatus.CONNECTING

    # ==========================================================

    def download(
        self,
        job: DownloadJob
    ) -> None:

        Logger.info(
            f"Download : {job.remote_file}"
        )

        job.status = JobStatus.DOWNLOADING

        self.service.download(

            job.remote_file,

            str(job.local_file)

        )

    # ==========================================================

    def verify(
        self,
        job: DownloadJob
    ) -> None:

        Logger.info("Verify Download")

        if job.local_file is None:

            raise FileNotFoundError(
                "Local file is empty."
            )

        if not job.local_file.exists():

            raise FileNotFoundError(
                str(job.local_file)
            )

        if job.local_file.stat().st_size == 0:

            raise ValueError(
                "Downloaded file size is zero."
            )

    # ==========================================================

    def cleanup(
        self,
        job: DownloadJob
    ) -> None:

        Logger.info("Cleanup")

        if self.service is not None:

            try:

                self.service.disconnect()

            except Exception:

                pass