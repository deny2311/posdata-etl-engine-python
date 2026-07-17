from app.core.database import Database


class DatabaseService:

    def __init__(self):

        self.db = Database()

    def health(self):

        return self.db.health_check()