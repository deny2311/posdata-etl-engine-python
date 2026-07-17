from app.services.transfer.ftp_service import FTPService
from app.services.transfer.sftp_service import SFTPService


class TransferFactory:

    @staticmethod
    def create(config):

        protocol = config.protocol.upper()

        if protocol == "FTP":

            return FTPService(config)

        if protocol == "SFTP":

            return SFTPService(config)

        raise Exception(
            f"Protocol tidak dikenali : {protocol}"
        )