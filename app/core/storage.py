from pathlib import Path
import shutil

from app.core.config import Config
from app.core.logger import Logger


class Storage:
    """
    Storage manager.

    Responsible for:

    - Create folders
    - Health check
    - Disk usage
    - Get storage path
    """

    def __init__(self):

        self.paths = {

            "download": Path(Config.get("DOWNLOAD_PATH")),

            "extract": Path(Config.get("EXTRACT_PATH")),

            "archive": Path(Config.get("ARCHIVE_PATH")),

            "failed": Path(Config.get("FAILED_PATH")),

            "logs": Path(Config.get("LOG_PATH")),

            "schema": Path(Config.get("SCHEMA_PATH"))

        }

    # ==========================================================
    # CREATE STORAGE
    # ==========================================================

    def create(self) -> None:

        for _, path in self.paths.items():

            if not path.exists():

                path.mkdir(
                    parents=True,
                    exist_ok=True
                )

                Logger.info(
                    f"Create folder : {path}"
                )

    # ==========================================================
    # HEALTH CHECK
    # ==========================================================

    def health_check(self) -> dict:

        result = {}

        for name, path in self.paths.items():

            status = {

                "exists": path.exists(),

                "write": False

            }

            if path.exists():

                try:

                    test = path / ".test"

                    test.write_text("OK")

                    test.unlink()

                    status["write"] = True

                except Exception:

                    status["write"] = False

            result[name] = status

        return result

    # ==========================================================
    # DISK
    # ==========================================================

    def disk(self) -> dict:

        total, used, free = shutil.disk_usage(".")

        return {

            "total": total,

            "used": used,

            "free": free

        }

    # ==========================================================
    # GET PATH
    # ==========================================================

    def get(self, name: str) -> Path:

        try:

            return self.paths[name]

        except KeyError:

            raise KeyError(
                f"Unknown storage path : {name}"
            )