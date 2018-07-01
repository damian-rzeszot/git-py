from .base import BaseCommand


class ConfigListCommand(BaseCommand):

    def run(self):
        config = self.repository.config()
        print(config.dump())
