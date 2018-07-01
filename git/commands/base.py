class BaseCommand:
    def __init__(self, repository):
        self._repository = repository

    @property
    def repository(self):
        return self._repository

    def run(self, *args):
        pass
