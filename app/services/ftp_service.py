from ftplib import FTP

from app.services.base_transfer_service import BaseTransferService
from app.core.logger import Logger


class FTPService(BaseTransferService):

    def __init__(self, config):

        self.config = config

        self.ftp = None

    def connect(self):

        self.ftp = FTP()

        self.ftp.connect(

            self.config.host,

            self.config.port,

            timeout=self.config.timeout

        )

        self.ftp.login(

            self.config.username,

            self.config.password

        )

        Logger.info(
            f"FTP Connected : {self.config.name}"
        )

        return True

    def disconnect(self):

        if self.ftp:

            self.ftp.quit()

            Logger.info(
                f"FTP Closed : {self.config.name}"
            )

    def list(self, path="."):

        return self.ftp.nlst(path)

    def exists(self, filename):

        return filename in self.ftp.nlst()

    def download(self, remote_file, local_file):

        with open(local_file, "wb") as f:

            self.ftp.retrbinary(

                f"RETR {remote_file}",

                f.write

            )