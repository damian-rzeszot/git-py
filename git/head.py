class Head:
	def __init__(self, repository):
		self._repository = repository

	@property
	def repository(self):
		return self._repository

	@property
	def value(self):
		db = self.repository.database
		value = db.read_file("HEAD").decode('utf8').strip()

		if value.startswith("ref: "):
			return value[5:]
		else:
			return value

	@property
	def branch(self):
		value = self.value

		if value.startswith("refs/heads/"):
			return value[11:]
		else:
			return None
