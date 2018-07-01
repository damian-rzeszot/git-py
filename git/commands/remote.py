from .base import BaseCommand
from ..utils import load_command


class RemoteCommand(BaseCommand):

    def run(self, *args):
        try:
            command = args[0]
        except IndexError:
            print("usage:")
            print("  remote show")
            exit(0)

        try:
            klass = load_command("remote_" + command)
            klass.run(*args)
        except ModuleNotFoundError:
            print("'remote %s' is not a command. See 'help'." % command)
            exit(1)
