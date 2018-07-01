from .base import BaseCommand


class HelpCommand(BaseCommand):

    def run(self, *args):
        print("usage:")
        print("  init")
        print("  config list")
        print("  remote show")
        print("  remote add <name> <url>")
        print("  remote remote <name>")
