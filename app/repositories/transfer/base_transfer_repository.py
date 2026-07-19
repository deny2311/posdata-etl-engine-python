from abc import ABC
from abc import abstractmethod

from app.models import TransferConfig


class BaseTransferRepository(ABC):
    """
    Base repository for transfer configuration.
    """

    @abstractmethod
    def get(
        self,
        store: str
    ) -> TransferConfig:
        """
        Return transfer configuration for a store.
        """
        raise NotImplementedError