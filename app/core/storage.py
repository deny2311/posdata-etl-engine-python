from pathlib import Path
import shutil

from app.core.config import Config
from app.core.logger import Logger


class Storage:

    def __init__(self):

        self.paths = {

            "download": Path(Config.get("DOWNLOAD_PATH")),

            "extract": Path(Config.get("EXTRACT_PATH")),

            "archive": Path(Config.get("ARCHIVE_PATH")),

            "failed": Path(Config.get("FAILED_PATH")),

            "logs": Path(Config.get("LOG_PATH")),

            "schema": Path(Config.get("SCHEMA_PATH"))

        }

    # =======================================
    # CREATE FOLDER
    # =======================================

    def create(self):

        for name, path in self.paths.items():

            if not path.exists():

                path.mkdir(
                    parents=True,
                    exist_ok=True
                )

                Logger.info(
                    f"Create Folder : {path}"
                )

    # =======================================
    # STORAGE STATUS
    # =======================================

    def health_check(self):

        result = {}

        for name, path in self.paths.items():

            result[name] = {

                "exists": path.exists(),

                "write": False

            }

            if path.exists():

                try:

                    test = path / ".test"

                    test.write_text("OK")

                    test.unlink()

                    result[name]["write"] = True

                except Exception:

                    result[name]["write"] = False

        return result

    # =======================================
    # DISK INFO
    # =======================================

    def disk(self):

        total, used, free = shutil.disk_usage(".")

        return {

            "total": total,

            "used": used,

            "free": free

        }