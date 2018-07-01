import zlib

from ..utils import load_object




class Object:

    def __init__(self, repository):
        self._repository = repository

    @property
    def repository(self):
        return self._repository


    @property
    def type(self):
        return self.__class__.__name__.lower()

    def dump(self):
        raise NotImplementedError()


    @classmethod
    def parse(klass, data, size):
        raise NotImplementedError()


    @classmethod
    def file(klass, repository, sha):
        path = "objects/%s/%s" % (sha[0:2], sha[2:])
        data = repository.database.read_file(path)
        header, data = zlib.decompress(data).split(b"\x00", 1)
        type, size = header.split(b" ")

        type = type.decode('utf8')
        size = int(size)

        klass = load_object(type)

        return klass.parse(repository, data, size)
