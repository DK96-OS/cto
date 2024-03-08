""" Detects Commit Line Prefix tags and generates formatted output.
"""

line_prefix_map = {
    'c': 'Create',
    'cr': 'Create',
    'd': 'Delete',
    'del': 'Delete',
    'f': 'Fix',
    'm': 'Move',
    'mv': 'Move',
    'r': 'Remove',
    're': 'Remove',
    't': 'Test',
    'u': 'Update',
    'up': 'Update',
    'upd': 'Update',
}


def map_line_prefix(line: str) -> str | None:
    """ Searches for a Prefix or a close match and returns a formatted line if found.
        Does not care about upper and lower case.
    :returns: The updated line or None if no prefix was found.
    """
    # Remove the prefix if it exists
    line = line.strip()
    if line.startswith('*'):
        line = line[1:].strip()

    # Extract the prefix
    prefix = line.split(' ')[0].lower()

    # Check if it is a valid prefix
    if prefix in line_prefix_map:
        return '* ' + line_prefix_map[prefix] + line[len(prefix):]

    return None
