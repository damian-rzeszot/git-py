from .base import BaseCommand


class BranchListCommand(BaseCommand):

	def run(self, *args):
		heads = self.repository.heads()
		longest = self.get_longest_head_name(heads.entries)

		for entry in heads.entries:
			infix = " " * (len(longest.name) - len(entry.name))
			print("%s%s  %s" % (entry.name, infix, entry.sha))


	def get_longest_head_name(self, entries):
		longest = None

		for entry in entries:
			if longest is None:
				longest = entry
			elif len(entry.name) > len(longest.name):
				longest = entry

		return longest
