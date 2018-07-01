from .base import BaseCommand


class RemoteShowCommand(BaseCommand):

    def run(self, *args):
        config = self.repository.config()

        for section in config.sections:
            if section.name != "remote":
                continue

            name = section.parameters
            fetch_url = section.get("url")
            push_url = section.get("pushurl") or fetch_url

            print("%s\t%s (fetch)" % (name, fetch_url))
            print("%s\t%s (push)" % (name, push_url))
