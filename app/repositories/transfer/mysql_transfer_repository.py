from app.models import TransferConfig

from .base_transfer_repository import BaseTransferRepository


class MysqlTransferRepository(BaseTransferRepository):
    """
    Read transfer configuration from MySQL.
    """

    def get(
        self,
        store: str
    ) -> TransferConfig:

        raise NotImplementedError(
            "MysqlTransferRepository is not implemented yet."
        )