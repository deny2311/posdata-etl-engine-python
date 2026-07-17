from app.services.transfer.base_transfer_service import BaseTransferService


class SFTPService(BaseTransferService):

    def __init__(self, config):

        self.config = config

    def connect(self):
        raise NotImplementedError()

    def disconnect(self):
        raise NotImplementedError()

    def list(self, path="."):
        raise NotImplementedError()

    def exists(self, filename):
        raise NotImplementedError()

    def download(self, remote_file, local_file):
        raise NotImplementedError()

    def upload(self, local_file, remote_file):
        raise NotImplementedError()