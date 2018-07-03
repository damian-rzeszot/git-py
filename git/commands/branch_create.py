from .base import BaseCommand
from ..reference import Reference


class BranchCreateCommand(BaseCommand):

	def run(self, name):
		heads = self.repository.references("heads")
		head = self.repository.head()

		if self.contains_head(name, heads):
			print("fatal: A branch named '%s' already exists." % name)
			exit(5)

		sha = head.sha
		ref = Reference(name, sha)

		heads.store(ref)


	def contains_head(self, name, heads):
		for entry in heads.entries:
			if entry.name == name:
				return True
		return False
