"""Methods handling File Names"""


def create_new_file_name(file_name: str, suffix: str) -> str:
    """
    Create a new file name with a suffix.

    Parameters:
    - file_name (str): The name of the file, including extension.
    - suffix (str): The suffix to append to the name of the file, before the extension.

    Returns:
    str - A String containing the File Name and the Suffix.
    """
    if (file_ext := _get_file_extension(file_name)) is None:
        # No File Extension
        return f"{file_name}{suffix}"
    # File Extension
    root_name = file_name[:-(len(file_ext) + 1)]
    return f"{root_name}{suffix}.{file_ext}"


def _get_file_extension(file_name: str) -> str | None:
    """
    Obtain the File Extension, if it exists.
        The Last extension in a multi-part extension is returned.

    Parameters:
    - file_name (str): The name of the File.

    Returns:
    str or None - The File Extension, or None.
    """
    try:
        index = len(file_name) - file_name[::-1].index('.')
        result = file_name[index:]
        if len(result) < 1:
            return None
        return result
    except:
        return None
