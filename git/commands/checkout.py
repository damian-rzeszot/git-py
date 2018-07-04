from .base import BaseCommand
from ..objects.object import Object



# checkout <branch>
class CheckoutCommand(BaseCommand):

	def run(self, name):
		heads = self.repository.references("heads")
		head = self.repository.head()

		if heads.contains(name):
			head.set_branch(name)
			commit = self.commit_from_sha(head.expanded_sha)
		else:
			commit = self.commit_from_sha(name)

			if not commit:
				print("error: branch/commit '%s' not found." % name)
				exit(7)

			head.set_sha(name)

		head.save()

		self.print_tree_recursive(commit.tree_object)


	def commit_from_sha(self, sha):
		try:
			object = Object.file(self.repository, sha)
		except FileNotFoundError:
			return None

		if object.type != "commit":
			return None

		return object


	def print_tree_recursive(self, tree, level = 0):
		prefix = " " * level * 4

		for entry in tree.entries:
			object = Object.file(self.repository, entry.sha)

			if object.type == "tree":
				print("%s + %s" % (prefix, entry.name))
				self.print_tree_recursive(Object.file(self.repository, entry.sha), level + 1)
			else:
				print("%s - %s" % (prefix, entry.name))
