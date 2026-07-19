from app.builders.store_code_builder import StoreCodeBuilder
from app.models import DownloadJob


class FilenameBuilder:
    """
    Build filename for POS daily data.

    Examples
    --------
    TSIS -> HR260701.SIS
    TRSA -> HR260701.RSA
    F1MP -> FR260701.1MP
    R01A -> CR260701.01A
    """

    @classmethod
    def build_download_filename(
        cls,
        job: DownloadJob
    ) -> str:
        """
        Build remote filename from DownloadJob.
        """

        prefix = StoreCodeBuilder.transfer_prefix(
            job.store
        )

        suffix = StoreCodeBuilder.transfer_suffix(
            job.store
        )

        date = job.trx_date.strftime("%y%m%d")

        return f"{prefix}{date}.{suffix}"