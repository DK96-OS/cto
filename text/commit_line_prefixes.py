""" Detects Commit Line Prefix tags and generates formatted output.
"""

generatedPrefixes = {
    'c': 'Create',
    'f': 'Fix',
    'm': 'Move',
    'r': 'Remove',
    't': 'Test',
    'u': 'Update',
}

# A Map from additional Commit Line Prefixes to their corresponding generators
expandingPrefixes = {
    'cr': 'c',
    'del': 'r',
    'mv': 'm',
    're': 'r',
    'up': 'u',
    'upd': 'u',
}


def update_line(line: str) -> str | None:
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
    if prefix in generatedPrefixes:
        return '* ' + generatedPrefixes[prefix] + line[len(prefix):]
    elif prefix in expandingPrefixes:
        return '* ' + generatedPrefixes[expandingPrefixes[prefix]] + line[len(prefix):]

    return None
