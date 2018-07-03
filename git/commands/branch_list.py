from .base import BaseCommand


class BranchListCommand(BaseCommand):

	def run(self, *args):
		references = self.repository.references("heads")
		head = self.repository.head()
		longest = self.get_longest_reference_name(references.entries)

		for entry in references.entries:
			infix = " " * (len(longest.name) - len(entry.name))

			if head.sha == entry.sha:
				print("* %s%s  %s" % (entry.name, infix, entry.sha))
			else:
				print("  %s%s  %s" % (entry.name, infix, entry.sha))


	def get_longest_reference_name(self, entries):
		longest = None

		for entry in entries:
			if longest is None:
				longest = entry
			elif len(entry.name) > len(longest.name):
				longest = entry

		return longest
