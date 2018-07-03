
class Reference:
	def __init__(self, name, sha):
		self._name = name
		self._sha = sha

	@property
	def name(self):
		return self._name

	@property
	def sha(self):
		return self._sha
