from app.models.transfer_config import TransferConfig
from app.core.config import Config


class FTPConfigRepository:

    @staticmethod
    def default():

        return TransferConfig(

            name="DEFAULT",

            protocol="FTP",

            host=Config.get("FTP_DEFAULT_HOST"),

            username=Config.get("FTP_DEFAULT_USER"),

            password=Config.get("FTP_DEFAULT_PASS"),

            port=int(Config.get("FTP_DEFAULT_PORT"))

        )

    @staticmethod
    def multi():

        return TransferConfig(

            name="MULTI",

            protocol="FTP",

            host=Config.get("FTP_MULTI_HOST"),

            username=Config.get("FTP_MULTI_USER"),

            password=Config.get("FTP_MULTI_PASS"),

            port=int(Config.get("FTP_MULTI_PORT"))

        )