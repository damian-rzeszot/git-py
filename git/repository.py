from .database import Database

class Repository:

    @property
    def database(self):
        return Database(self)
