from .base import BaseCommand
from ..reference import Reference


class BranchCreateCommand(BaseCommand):

	def run(self, name):
		heads = self.repository.references("heads")
		head = self.repository.head()

		if heads.contains(name):
			print("fatal: A branch named '%s' already exists." % name)
			exit(5)

		ref = Reference(name, head.expanded_sha)

		heads.store(ref)
