from .object import Object





class Commit(Object):

	def __init__(self, repository, tree, parents, author, committer, message):
		self._repository = repository
		self._tree = tree
		self._parents = parents
		self._author = author
		self._committer = committer
		self._message = message

	@property
	def tree(self):
		return self._tree

	@property
	def parents(self):
		return self._parents

	@property
	def author(self):
		return self._author

	@property
	def committer(self):
		return self._committer

	@property
	def message(self):
		return self._message

	@property
	def summary(self):
		return self.message.split('\n', 1)[0]

	@property
	def tree_object(self):
		return self.__class__.file(self.repository, self.tree)

	def __repr__(self):
		return "<Commit tree:%s parents:%s msg:'%s'>" % (self.tree, self.parents, self.message)


	@classmethod
	def parse(klass, repository, data, size):
		dict, message = parse(data)
		return klass(repository, dict['tree'], dict['parent'], dict['author'], dict['committer'], message)



def parse(data):
	dict = {}

	header, message = data.decode('utf8').split("\n\n", 1)

	for line in header.split("\n"):
		key, value = line.split(" ", 1)
		if key == "parent":
			dict[key] = dict.get(key) or []
			dict[key].append(value)
		else:
			dict[key] = value

	return dict, message
