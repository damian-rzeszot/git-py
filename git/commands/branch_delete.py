from .base import BaseCommand
from ..reference import Reference


class BranchDeleteCommand(BaseCommand):

	def run(self, name):
		heads = self.repository.references("heads")
		head = self.repository.head()

		if not heads.contains(name):
			print("error: branch '%s' not found." % name)
			exit(5)

		self.repository.database.delete_file("refs/heads/%s" % name)
