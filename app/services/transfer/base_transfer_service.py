from abc import ABC
from abc import abstractmethod


class BaseTransferService(ABC):

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def list(self, path="."):
        pass

    @abstractmethod
    def exists(self, filename):
        pass

    @abstractmethod
    def download(self, remote_file, local_file):
        pass

    @abstractmethod
    def upload(self, local_file, remote_file):
        pass