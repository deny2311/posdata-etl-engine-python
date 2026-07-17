import platform
import sys

from app.core.config import Config

from app.services.database_service import DatabaseService
from app.services.storage_service import StorageService


class SystemCheckService:

    def __init__(self):

        self.database = DatabaseService()

        self.storage = StorageService()

    def run(self):

        return {

            "application": {

                "name": Config.app_name(),

                "version": Config.version(),

                "environment": Config.env()

            },

            "python": {

                "version": platform.python_version(),

                "platform": platform.system(),

                "detail": sys.version

            },

            "database": self.database.health(),

            "storage": self.storage.health(),

            "disk": self.storage.disk()

        }