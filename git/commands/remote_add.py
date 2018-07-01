from .base import BaseCommand
from ..utils import load_command
from ..config import Section



class RemoteAddCommand(BaseCommand):

    def run(self, name, url):
        config = self.repository.config()

        if config.remote_exists(name):
            print("fatal: remote '%s' already exists." % name)
            exit(0)

        section = Section("remote", name)
        section.set("url", url)
        section.set("fetch", "+refs/heads/*:refs/remotes/%s/*" % name)

        config.append(section)
        config.save()
