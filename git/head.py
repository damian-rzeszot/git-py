class Head:
	def __init__(self, repository):
		self._repository = repository

	@property
	def repository(self):
		return self._repository

	@property
	def sha(self):
		db = self.repository.database
		value = db.read_file("HEAD").decode('utf8')

		if value.startswith("ref: "):
			return db.read_file(value[5:].strip()).strip().decode('utf8')
		else:
			return value
