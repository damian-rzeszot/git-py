from .database import Database
from .config import Config



class Repository:

    @property
    def database(self):
        return Database(self)

    def config(self):
        return Config(self)
