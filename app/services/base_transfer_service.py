from abc import ABC, abstractmethod


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