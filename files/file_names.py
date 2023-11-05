""" Manage File Names """


def create_new_file_name(
        file_name: str,
        suffix: str
) -> str:
    """ Create a new file name with a suffix.
    """
    if file_name.endswith('.txt'):
        return f"{file_name[:-4]}{suffix}.txt"
    else:
        return f"{file_name}{suffix}"
