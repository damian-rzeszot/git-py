from .object import Object





class Commit(Object):

    def __init__(self, tree, parents, author, committer, message):
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
