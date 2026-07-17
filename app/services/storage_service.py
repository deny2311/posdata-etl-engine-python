from app.core.storage import Storage


class StorageService:

    def __init__(self):

        self.storage = Storage()

    def health(self):

        self.storage.create()

        return self.storage.health_check()

    def disk(self):

        return self.storage.disk()