from .env_transfer_repository import EnvTransferRepository


class TransferRepository:
    """
    Repository facade.
    """

    def __new__(cls):

        return EnvTransferRepository()