from .database import Database
from .config import Config
from .objects.object import Object
from .reference import Reference
from .head import Head


class Repository:

    @property
    def database(self):
        return Database(self)

    def config(self):
        return Config(self)

    def object(self, sha):
        return Object.file(self, sha)

    def references(self, kind):
        return ReferencesWrapper(self, kind)

    def head(self):
        return Head(self)





class ReferencesWrapper:
    def __init__(self, repository, kind):
        self._repository = repository
        self._kind = kind

    @property
    def repository(self):
        return self._repository

    @property
    def kind(self):
        return self._kind

    def contains(self, name):
        for entry in self.entries:
            if entry.name == name:
                return True
        return False

    @property
    def entries(self):
        db = self.repository.database
        heads = []

        for entry in list(db.list_directory("refs/%s" % self.kind)):
            content = db.read_file("refs/%s/%s" % (self.kind, entry)).strip().decode('utf8')
            heads.append(Reference(entry, content))

        return heads

    def store(self, head):
        path = "refs/%s/%s" % (self.kind, head.name)
        self.repository.database.write_file(path, head.sha)
