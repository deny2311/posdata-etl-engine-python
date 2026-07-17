from pathlib import Path
from dotenv import load_dotenv
import os

BASE_DIR = Path(__file__).resolve().parents[2]

load_dotenv(BASE_DIR / ".env")


class Config:

    @staticmethod
    def get(key, default=None):
        return os.getenv(key, default)

    @staticmethod
    def app_name():
        return Config.get("APP_NAME")

    @staticmethod
    def version():
        return Config.get("APP_VERSION")

    @staticmethod
    def env():
        return Config.get("APP_ENV")

    @staticmethod
    def debug():
        return Config.get("APP_DEBUG")

    @staticmethod
    def db_host():
        return Config.get("DB_HOST")

    @staticmethod
    def db_port():
        return Config.get("DB_PORT")

    @staticmethod
    def db_name():
        return Config.get("DB_NAME")

    @staticmethod
    def db_user():
        return Config.get("DB_USER")

    @staticmethod
    def db_pass():
        return Config.get("DB_PASS")