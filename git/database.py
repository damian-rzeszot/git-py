from os import mkdir
from os.path import exists



class Database:
    def __init__(self, repository):
        self._repository = repository

    def read_file(self, path):
        path = ".git/%s" % path

        file = open(path, "r")
        data = file.read()
        file.close()

        return data

    def write_file(self, path, content):
        path = ".git/%s" % path

        file = open(path, "w")
        file.write(content)
        file.close()


    def create_file(self, path, content = ""):
        if exists(".git/%s" % path):
            print("! file exists %s" % (".git/%s" % path))
        else:
            self.write_file(path, content)

    def create_directory(self, path):
        path = ".git/%s" % path

        try:
            mkdir(path)
        except FileExistsError:
            print("! directory exists %s" % path)
