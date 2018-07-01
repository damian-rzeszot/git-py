from .base import BaseCommand
from ..utils import load_command


class ConfigCommand(BaseCommand):

    def run(self, *args):
        try:
            command = args[0]
        except IndexError:
            print("usage:")
            print("  config list")
            exit(0)

        try:
            klass = load_command("config_" + command)
            object = klass(self.repository)
            object.run(*args[1:])
        except ModuleNotFoundError:
            print("'config %s' is not a command. See 'help'." % command)
            exit(1)
        except TypeError:
            print("'config %s' is not a correct use. See 'help'." % command)
            exit(2)
