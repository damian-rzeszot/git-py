from .base import BaseCommand


class InitCommand(BaseCommand):

    def run(self, *args):
        db = self.repository.database

        db.create_directory('objects')

        db.create_directory('refs')
        db.create_directory('refs/heads')

        db.create_file('HEAD', "ref: refs/heads/master")
