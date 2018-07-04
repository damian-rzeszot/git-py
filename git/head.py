class Head:
	def __init__(self, repository):
		self._repository = repository
		self._value = repository.database.read_file("HEAD").decode('utf8').strip()

	@property
	def repository(self):
		return self._repository

	@property
	def value(self):
		return self._value

	def set_branch(self, name):
		self._value = "ref: refs/heads/%s" % name

	def set_sha(self, sha):
		self._value = sha

	def __repr__(self):
		return "<HEAD %s>" % self.value

	def save(self):
		self.repository.database.write_file("HEAD", self.value)

	@property
	def branch(self):
		if self.value.startswith("ref: refs/heads/"):
			return self.value[16:]
		else:
			return None

	@property
	def expanded_sha(self):
		if self.branch:
			return self.repository.database.read_file("refs/heads/%s" % self.branch).decode('utf8').strip()
		else:
			return self.sha

	@property
	def sha(self):
		if self.value.startswith("ref: refs/heads/"):
			return None
		else:
			return self.value
