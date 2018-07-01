from .object import Object





class Tree(Object):

    def __init__(self, entries):
        self._entries = entries

    @property
    def entries(self):
        return self._entries





class Entry:
    def __init__(self, mode, sha, name):
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
