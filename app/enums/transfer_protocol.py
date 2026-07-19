from enum import Enum


class TransferProtocol(str, Enum):
    FTP = "FTP"

    SFTP = "SFTP"

    LOCAL = "LOCAL"