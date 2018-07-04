from .base import BaseCommand

# checkout <branch>
class CheckoutCommand(BaseCommand):

	def run(self, name):
		heads = self.repository.references("heads")

		if not heads.contains(name):
			print("error: branch '%s' not found." % name)
			exit(6)

		head = self.repository.head()
		head.set_branch(name)
		head.save()

		# replace working tree with commit
