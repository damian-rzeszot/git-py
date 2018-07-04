from .object import Object





class Blob(Object):

    def __init__(self, repository, content, size):
        super().__init__(repository)

        self._content = content
        self._size = size

    @property
    def size(self):
        return self._size

    @property
    def content(self):
        return self._content

    def dump(self):
        return b"%s %d\x00%s" % (self.type.encode('utf-8'), self.size, self.content)

    def __repr__(self):
        return "<Blob size:%s>" % (self.size)


    @classmethod
    def parse(klass, repository, data, size):
        return klass(repository, data, size)
