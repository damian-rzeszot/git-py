from .database import Database
from .config import Config
from .objects.object import Object
from .reference import Reference


class Repository:

    @property
    def database(self):
        return Database(self)

    def config(self):
        return Config(self)

    def object(self, sha):
        return Object.file(self, sha)

    def heads(self):
        return HeadsWrapper(self)



class HeadsWrapper:
	def __init__(self, repository):
		self._repository = repository

	@property
	def repository(self):
		return self._repository

	@property
	def entries(self):
		db = self.repository.database
		heads = []

		for entry in list(db.list_directory("refs/heads")):
			content = db.read_file("refs/heads/%s" % entry).strip().decode('utf8')
			heads.append(Reference(entry, content))

		return heads

	def store(self, head):
		pass
