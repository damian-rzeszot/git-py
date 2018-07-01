from sys import argv

from git.repository import Repository
from git.utils import *



try:
    command = argv[1]
except IndexError:
    command = "help"

try:
    klass = load_command(command)
except ModuleNotFoundError:
    print("'%s' is not a command. See 'help'." % argv[1])
    exit(1)


arguments = argv[2:]
repository = Repository()

object = klass(repository)

try:
    object.run(*arguments)
except TypeError:
    print("'%s' is not a correct use. See 'help'." % command)
    exit(2)
