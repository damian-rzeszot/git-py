from .base import BaseCommand
from ..utils import load_command


class BranchCommand(BaseCommand):

    def run(self, *args):
        try:
            command = args[0]
        except IndexError:
            print("usage:")
            print("  branch list")
            print("  branch create <name>")
            print("  branch delete <name>")
            exit(0)

        try:
            klass = load_command("branch_" + command)
            object = klass(self.repository)
            object.run(*args[1:])
        except ModuleNotFoundError:
            print("'branch %s' is not a command. See 'help'." % command)
            exit(1)
        except TypeError:
            print("'branch %s' is not a correct use. See 'help'." % command)
            exit(2)
