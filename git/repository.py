from .database import Database
from .config import Config
from .objects.object import Object



class Repository:

    @property
    def database(self):
        return Database(self)

    def config(self):
        return Config(self)

    def object(self, sha):
        return Object.file(self, sha)
