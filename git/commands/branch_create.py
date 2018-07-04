from .base import BaseCommand
from ..reference import Reference


class BranchCreateCommand(BaseCommand):

	def run(self, name):
		heads = self.repository.references("heads")
		head = self.repository.head()

		if heads.contains(name):
			print("fatal: A branch named '%s' already exists." % name)
			exit(5)

		sha = head.sha
		ref = Reference(name, sha)

		heads.store(ref)
