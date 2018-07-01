from .base import BaseCommand


class RemoteRemoveCommand(BaseCommand):

    def run(self, name):
        config = self.repository.config()

        if not config.remote_exists(name):
            print("fatal: No such remote '%s'" % name)
            exit(0)

        config.remove_section_if(lambda x: x.name == "remote" and x.parameters == name)
        config.save()
