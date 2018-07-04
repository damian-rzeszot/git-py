from .object import Object
from binascii import b2a_hex




class Tree(Object):

	def __init__(self, repository, entries):
		self._repository = repository
		self._entries = entries

	@property
	def entries(self):
		return self._entries

	def __repr__(self):
		return "<Tree %s>" % self.entries

	@classmethod
	def parse(klass, repository, data, size):
		return klass(repository, parse(repository, data, size))



def parse(repository, data, size):
	entries = []
	i = 0

	while i < size:
		mode = ""
		name = ""

		while data[i] != 0x20:
			mode += chr(data[i])
			i += 1

		i += 1 # space

		while data[i] != 0x0:
			name += chr(data[i])
			i += 1

		i += 1

		sha = data[i:i+20]
		i += 20

		entries.append(Entry(repository, mode, name, b2a_hex(sha).decode('utf8')))

	return entries



class Entry:
	def __init__(self, repository, mode, name, sha):
		self._mode = mode
		self._sha = sha
		self._name = name

	@property
	def mode(self):
		return self._mode

	@property
	def sha(self):
		return self._sha

	@property
	def name(self):
		return self._name

	def __repr__(self):
		return "<TreeEntry %s x %s>" % (self.name, self.sha)
