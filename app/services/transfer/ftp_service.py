from ftplib import FTP

from app.core.logger import Logger

from app.services.transfer.base_transfer_service import BaseTransferService


class FTPService(BaseTransferService):

    def __init__(self, config):

        self.config = config

        self.client = None

    # -------------------------------------

    def connect(self):

        Logger.info(
            f"Connect FTP : {self.config.host}"
        )

        self.client = FTP()

        self.client.connect(
            host=self.config.host,
            port=self.config.port,
            timeout=self.config.timeout
        )

        self.client.login(
            self.config.username,
            self.config.password
        )

        self.client.set_pasv(
            self.config.passive
        )

        Logger.info("FTP Connected")

        return True

    # -------------------------------------

    def disconnect(self):

        if self.client:

            self.client.quit()

            Logger.info("FTP Closed")

    # -------------------------------------

    def list(self, path="."):

        return self.client.nlst(path)

    # -------------------------------------

    def exists(self, filename):

        return filename in self.client.nlst()

    # -------------------------------------

    def download(
        self,
        remote_file,
        local_file
    ):

        with open(local_file, "wb") as f:

            self.client.retrbinary(
                f"RETR {remote_file}",
                f.write
            )

    # -------------------------------------

    def upload(
        self,
        local_file,
        remote_file
    ):

        with open(local_file, "rb") as f:

            self.client.storbinary(
                f"STOR {remote_file}",
                f
            )