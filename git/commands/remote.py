from .base import BaseCommand
from ..utils import load_command


class RemoteCommand(BaseCommand):

    def run(self, *args):
        try:
            command = args[0]
        except IndexError:
            print("usage:")
            print("  remote show")
            print("  remote add <name> <url>")
            exit(0)

        try:
            klass = load_command("remote_" + command)
            object = klass(self.repository)
            object.run(*args[1:])
        except ModuleNotFoundError:
            print("'remote %s' is not a command. See 'help'." % command)
            exit(1)
        except TypeError:
            print("'remote %s' is not a correct use. See 'help'." % command)
            exit(2)
