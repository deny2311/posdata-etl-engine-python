from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

from app.core.config import Config
from app.core.logger import Logger


class Database:

    def __init__(self):

        self.host = Config.get("DB_HOST")
        self.port = Config.get("DB_PORT")
        self.database = Config.get("DB_NAME")
        self.user = Config.get("DB_USER")
        self.password = Config.get("DB_PASS")

        self.engine = None

    # ==========================================
    # CONNECT
    # ==========================================

    def connect(self):

        if self.engine is not None:
            return self.engine

        url = (
            f"mysql+pymysql://{self.user}:{self.password}"
            f"@{self.host}:{self.port}/{self.database}"
            "?charset=utf8mb4"
        )

        try:

            self.engine = create_engine(
                url,
                pool_pre_ping=True,
                pool_recycle=3600,
                pool_size=5,
                max_overflow=10,
                future=True,
                echo=False
            )

            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))

            Logger.info("Database Connected")

            return self.engine

        except Exception as e:

            Logger.error(f"Database Error : {e}")

            raise

    # ==========================================
    # HEALTH CHECK
    # ==========================================

    def health_check(self):

        try:

            self.connect()

            with self.engine.connect() as conn:

                version = conn.execute(
                    text("SELECT VERSION()")
                ).scalar()

                charset = conn.execute(
                    text("SELECT @@character_set_database")
                ).scalar()

            return {

                "connected": True,

                "host": self.host,

                "database": self.database,

                "user": self.user,

                "version": version,

                "charset": charset

            }

        except Exception as e:

            return {

                "connected": False,

                "error": str(e)

            }

    # ==========================================
    # CHECK CONNECTION
    # ==========================================

    def is_connected(self):

        try:

            self.connect()

            with self.engine.connect() as conn:

                conn.execute(text("SELECT 1"))

            return True

        except Exception:

            return False

    # ==========================================
    # QUERY DATAFRAME
    # ==========================================

    def query(self, sql):

        self.connect()

        return pd.read_sql(text(sql), self.engine)

    # ==========================================
    # EXECUTE SQL
    # ==========================================

    def execute(self, sql):

        self.connect()

        with self.engine.begin() as conn:

            conn.execute(text(sql))

    # ==========================================
    # EXECUTE SCALAR
    # ==========================================

    def scalar(self, sql):

        self.connect()

        with self.engine.connect() as conn:

            return conn.execute(
                text(sql)
            ).scalar()

    # ==========================================
    # CLOSE
    # ==========================================

    def close(self):

        if self.engine:

            self.engine.dispose()

            Logger.info("Database Closed")