from .base import BaseCommand
from ..reference import Reference


class BranchDeleteCommand(BaseCommand):

	def run(self, name):
		heads = self.repository.references("heads")
		head = self.repository.head()

		if not self.contains_head(name, heads):
			print("error: branch '%s' not found." % name)
			exit(5)

		self.repository.database.delete_file("refs/heads/%s" % name)


	def contains_head(self, name, heads):
		for entry in heads.entries:
			if entry.name == name:
				return True
		return False
