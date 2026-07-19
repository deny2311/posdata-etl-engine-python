from app.core.config import Config
from app.enums import TransferProtocol
from app.models import TransferConfig

from .base_transfer_repository import BaseTransferRepository


class EnvTransferRepository(BaseTransferRepository):
    """
    Read transfer configuration from .env
    """

    def __init__(self):

        self.multi_store = {
            "TT9F",
        }

    def get(
        self,
        store: str
    ) -> TransferConfig:

        if store in self.multi_store:
            return self._multi()

        return self._default()

    def _default(self) -> TransferConfig:

        return TransferConfig(

            name="DEFAULT",

            protocol=TransferProtocol.FTP,

            host=Config.get("FTP_DEFAULT_HOST"),

            username=Config.get("FTP_DEFAULT_USER"),

            password=Config.get("FTP_DEFAULT_PASS"),

            port=int(Config.get("FTP_DEFAULT_PORT"))
        )

    def _multi(self) -> TransferConfig:

        return TransferConfig(

            name="MULTI",

            protocol=TransferProtocol.FTP,

            host=Config.get("FTP_MULTI_HOST"),

            username=Config.get("FTP_MULTI_USER"),

            password=Config.get("FTP_MULTI_PASS"),

            port=int(Config.get("FTP_MULTI_PORT"))
        )