""" Commit Line Class and supporting methods.
"""
from .commit_line_prefixes import map_line_prefix

# Subject is separated from content by a separator
subject_separators = ('-', '+')

# The Minimum Subject Length, otherwise line is content
min_subject_length = 2


class CommitLine:
    """ Represents a Line in a Commit Message.

    Internal Properties:
    - _subject (str | None): The first section of the line before the separator (the whole line), or None
    - _content (str | None): The section of the string after the first separator, or None.
    - _subject_separator_index (int | None): The index of the separator in the updated_line, or None.
    - _init_line (str): The initial line passed to the CommitLine constructor.
    - _updated_line (str): The processed init line (strip space, map_line_prefix).
    """

    def __init__(
        self, line: str
    ):
        """
        Parameters:
        - line (str): The string containing the commit line input.
        """
        updated_line = line.strip()
        # Expand Commit Line Prefixes
        if (expanded_line := map_line_prefix(updated_line)) is not None:
            updated_line = expanded_line
        # Find the Subject Separator
        if (separator_index := find_subject_separator(updated_line)) is None:
            # When there is no separator, Subject is given the line
            self._subject = None if len(updated_line) < 1 else updated_line
            self._content = None
        elif separator_index + 1 >= len(updated_line):
            # Separator at end of line
            self._subject = updated_line[:separator_index].rstrip()
            self._content = None
        else:
            # Check Subject
            subject_line = updated_line[:separator_index].rstrip()
            self._subject = None if len(subject_line) < 1 else subject_line
            # Check Content
            content_line = updated_line[separator_index + 1:].lstrip()
            self._content = None if len(content_line) < 1 else content_line
        self._subject_separator_index = separator_index
        self._init_line = line
        self._updated_line = updated_line

    def get_subject(self) -> str | None:
        """ Obtain the Subject, if present.
        """
        return self._subject

    def get_separator(self) -> str:
        """ Obtain the Separator between the Subject and Content.
            Is empty str when separator not found.
        """
        if (index := self._subject_separator_index) is None:
            return ""
        return self._updated_line[index]

    def get_content(self) -> str | None:
        """ Obtain the Content section of the Commit Line, if present.
        """
        return self._content

    def get_input_line(self) -> str:
        """ Return the Line that was given as input.
        """
        return self._init_line

    def __str__(self):
        """ Obtain the Processed Commit Line as a String.
        """
        return self._updated_line


def merge_lines(
        line_a: CommitLine,
        line_b: CommitLine
) -> CommitLine:
    """ Merge two Commit Lines into one.
    """
    subject = line_a.get_subject()
    separator = _choose_separator(line_a, line_b)
    # Compare the content of the two lines
    content_a = line_a.get_content()
    content_b = line_b.get_content()
    # If both lines have content, merge the content
    if content_a is not None and content_b is not None:
        # If the content of the first line ends with a period, remove the period
        if content_a.endswith('.'):
            content_a = content_a[:-1]
        # If the content of the first line ends with a space, remove the space
        if content_a.endswith(' '):
            content_a = content_a.rstrip()
        # If the content of the first line ends with a comma, remove the comma
        if content_a.endswith(','):
            content_a = content_a[:-1]
        # If the content of the second line starts with a capital letter, convert the first letter to lowercase
        if content_b[0].isupper():
            content_b = content_b[0].lower() + content_b[1:]
        # If the content of the second line starts with a period, remove the period
        if content_b.startswith('.'):
            content_b = content_b[1:]
        # If the content of the second line starts with a space, remove the space
        if content_b.startswith(' '):
            content_b = content_b.lstrip()
        # If the content of the second line starts with a comma, remove the comma
        if content_b.startswith(','):
            content_b = content_b[1:]
        # Ensure only one space between content_a and content_b
        content = content_a + ', ' + content_b
    # If only one line has content, use that content
    elif content_a is not None:
        content = content_a
    elif content_b is not None:
        content = content_b
    # If neither line has content, use None
    else:
        content = None
    # Create the new Commit Line
    if subject is None:
        if content is None:
            new_line = ""
        else:
            new_line = content
    else:
        if content is None:
            new_line = subject
        else:
            new_line = str.format(f"{subject} {separator} {content}")
    return CommitLine(new_line)


def _choose_separator(
    line_a: CommitLine,
    line_b: CommitLine,
) -> str:
    """ Choose the separator to use for the merged line.
    """
    sep_a = line_a.get_separator()
    sep_b = line_b.get_separator()
    # If both lines have the same separator, use that separator
    if sep_a == sep_b:
        return sep_a
    # If one line has no separator, use the other line's separator
    if len(sep_a) < 1:
        if len(sep_b) < 1:
            # If neither line has a separator, use the default separator
            return subject_separators[0]
        return sep_b
    if len(sep_b) < 1:
        return sep_a
    # If both lines have separators, use the separator that appears first in the subject_separators tuple
    for sep in subject_separators:
        if sep_a == sep:
            return sep_a
        if sep_b == sep:
            return sep_b
    # If none of the above conditions are met, use the first separator in the subject_separators tuple
    return subject_separators[0]


def find_subject_separator(
    line: str
) -> int | None:
    """ Find the Subject separator.
        Returns None if separator not found.
    """
    idx_list = (line.find(sep) for sep in subject_separators)
    min_idx = -1
    for i in idx_list:
        if min_subject_length <= i:
            if min_idx == -1 or i < min_idx:
                min_idx = i
    # Only Return Positive Indices
    return min_idx if min_idx >= min_subject_length else None
