"""Container for a category of text
"""
from .commit_line import CommitLine, merge_lines


def strip_header(
        text: str
) -> str:
    """ Headers are the High Level Labels on Groups.
        Remove any leading or trailing whitespace.
    """
    return text.strip().lstrip('\*').strip(' ')


class CommitLineGroup:
    """ A group of related commit messages.
    """

    def __init__(
            self,
            header: str | None,
            lines: list[str] | list[CommitLine] | tuple[str] | tuple[CommitLine] = None
    ):
        """
        Parameters:
        - header (str | None): The Header string for the Group.
        - lines (list[str] | list[CommitLine] | tuple[str] | tuple[CommitLine]): A collection of string or CommitLine objects.
        """
        if header is None or len(header) == 0:
            self._header = None
        else:
            self._header = strip_header(header)
        # Convert Text Lines into Commit Lines
        self._commit_lines: list[CommitLine] = []
        if lines is None:
            return
        elif isinstance(lines, list):
            for ln in lines:
                self.add_line(ln)
        elif isinstance(lines, tuple):
            for ln in lines:
                self.add_line(ln)
        else:
            raise ValueError(type(lines))

    def get_header(self) -> str:
        """ Obtain the Header of the Commit Text Group.
            May return an empty string if the group is headless.
        """
        if self._header is None:
            return ""
        return self._header

    def get_line_count(self) -> int:
        """ Obtain the number of Lines in the Commit Group.
        """
        return len(self._commit_lines)

    def add_line(
            self,
            line: str | CommitLine
    ) -> bool:
        """ Add a new line to this group.
        """
        if isinstance(line, str):
            if len(line) < 1:
                return False
            self._commit_lines.append(CommitLine(line))
            return True
        elif isinstance(line, CommitLine):
            self._commit_lines.append(line)
            return True
        return False

    def sort(self):
        """ Sort the lines in this group.
        """
        self._commit_lines.sort(
            key=lambda line: str(line)
        )

    def process_lines(self) -> bool:
        """ Process all Lines in this Group:
            Combine Lines with the same Subject,
            Returns true if there were at least 2 Lines
        """
        # Skip operation if fewer than 2 Lines
        index = 1
        # Find Lines with matching Subjects and combine them into a single Line
        while index < len(self._commit_lines):
            line_a = self._commit_lines[index - 1]
            # If the Subjects are None, do not merge
            if line_a.get_subject() is None:
                index += 1
                continue
            line_b = self._commit_lines[index]
            if line_b.get_subject() is None:
                index += 2
                continue
            if line_a.get_subject() == line_b.get_subject():
                # Merge Lines
                line_a = merge_lines(line_a, line_b)
                # Replace merged line
                self._commit_lines[index - 1] = line_a
                # Remove merged line
                self._commit_lines.pop(index)
            else:
                index += 1
        return True

    def autoprocess(self):
        """ Apply Default processing operations:
            Sort Lines alphabetically,
            Merge Lines with matching subjects,
        """
        self.sort()
        self.process_lines()

    def get_lines_as_commit_line_array(self) -> list[CommitLine]:
        """ Obtain all of the Lines in the Group as a List of CommitLine objects.
        """
        return [s for s in self._commit_lines]

    def get_lines_as_str_array(self) -> list[str]:
        """ Obtain all of the Lines in the Group as a List of Strings.
        """
        return [str(s) for s in self._commit_lines]

    def __str__(self):
        """ Obtain the whole Commit Text Group as a String.
        """
        line_items = "\n".join(str(s) for s in self._commit_lines)
        if self._header is None:
            return line_items
        # Combine Header and Lines
        if len(line_items.strip()) < 1:
            return self.get_header()
        return self.get_header() + "\n" + line_items


def merge_groups(
        self: CommitLineGroup,
        other: CommitLineGroup
) -> CommitLineGroup:
    """ Combine Two Text Groups into a new Text Group.
        Assumes that the Headers are equal, uses the first Group's header.
    """
    # Create a new group to avoid modifying either input group
    new_group = CommitLineGroup(
        self.get_header(),
        self.get_lines_as_commit_line_array()
    )
    # Add all lines from the Other group
    for line in other.get_lines_as_commit_line_array():
        new_group.add_line(line)
    # Sort all Lines in the Merged Group, and process them together
    new_group.autoprocess()
    return new_group
