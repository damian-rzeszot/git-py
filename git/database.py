from os import mkdir
from os.path import exists



class Database:
    def __init__(self, repository):
        self._repository = repository

    def create_file(self, path, content = ""):
        path = ".git/%" % path

        if exists(path):
            print("! file exists %s" % path)
        else:
            file = open(path, "w")
            file.write(content)
            file.close()

    def create_directory(self, path):
        path = ".git/%" % path

        try:
            mkdir(path)
        except FileExistsError:
            print("! directory exists %s" % path)
