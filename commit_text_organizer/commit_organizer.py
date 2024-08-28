"""Processes an input string into groups of text.
"""
from .commit_line_group import CommitLineGroup, merge_groups
from .input_data import InputData


class CommitOrganizer:
	""" The High level data structure that makes it easy to organize commit text.
	"""

	def __init__(self):
		"""
		Properties:
		- groups (list[CommitLineGroup]): The list of Commit Line Groups.
		- pr_group (CommitLineGroup | None): Used to collect PR lines, and merge them into one group.
		"""
		self.groups = []
		# The PR group will be added to the Groups, so it can be sorted
		self.pr_group = None

	def receive_data(
			self,
			data: str
	):
		""" Clear existing data, then receive new data.
		"""
		self.clear()
		lines = data.strip().split('\n')
		#
		active_group = None
		newline_count = 0
		for next_line in lines:
			li = next_line.strip()
			if len(li) < 1:
				newline_count += 1
				if newline_count > 1:
					active_group = None
			elif li.endswith(':'):
				# Header
				active_group = CommitLineGroup(li)
				self.groups.append(active_group)
				newline_count = 0
			elif li.startswith('*'):
				# Headless Commit Line or Group
				if active_group is not None:
					active_group.add_line(li)
				else:
					active_group = CommitLineGroup(
						None, (li.strip(),)
					)
					self.groups.append(active_group)
				newline_count = 0
			# Identify PullRequest Lines: do not start with * but end with (# 5)
			elif li.endswith(')') and li.count('(') == 1 and li.count('#') == 1:
				# Record Line in a PullRequest only member of CommitTextOrganizer
				self.add_pull_request_line(li)
				newline_count = 0
			else:
				print(f"Unknown Line {str(1 + lines.index(next_line))} : {li}")

	def add_pull_request_line(
			self,
			line: str
	):
		""" Add a line to the PullRequest Group.
		"""
		if self.pr_group is None:
			self.pr_group = CommitLineGroup("Pull Requests:")
			self.groups.append(self.pr_group)
		# Prepend a * to the line
		self.pr_group.add_line('* ' + line)

	def clear(self):
		""" Removes all temporary data.
		"""
		self.groups.clear()
		self.pr_group = None

	def autoprocess(self):
		""" Perform a series of reasonable processes, including:
			sort(), autoprocess_groups(),
		"""
		self.sort()
		self.autoprocess_groups()

	def sort(self):
		""" Sort Text Groups by Header.
		"""
		self.groups.sort(key=CommitLineGroup.get_header)
		i = 0
		while i + 1 < len(self.groups):
			g0 = self.groups[i]
			if len(g0.get_header()) == 0:
				i += 1
				continue
			g1 = self.groups[i + 1]
			if g0.get_header() == g1.get_header():
				self.groups[i] = merge_groups(g0, g1)
				del self.groups[i + 1]
			else:
				i += 1

	def autoprocess_groups(self):
		""" Apply default processing to each group:
			Sort Lines alphabetically,
			Merge Lines with matching subjects,
		"""
		for g in self.groups:
			g.autoprocess()

	def output_all_groups(self) -> str | None:
		""" Package all groups into a string.
		"""
		if len(self.groups) == 0:
			return None
		package = ""
		for g in self.groups:
			group_string = str(g)
			if len(group_string) < 1:
				continue
			# Only add a new line if there is another group after this one
			if g != self.groups[-1]:
				group_string += '\n'
			package += group_string + "\n"
		return package


def process_with_cto(input_data: InputData) -> str:
    """Process the Input Text with Commit Text Organizer
    """
    cto = CommitOrganizer()
    cto.receive_data(input_data.text_input)
    cto.autoprocess() # Default Processing Operations
    return cto.output_all_groups()
