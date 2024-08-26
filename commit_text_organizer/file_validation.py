"""File Validation Methods.
    These Methods all raise SystemExit exceptions.
"""
from pathlib import Path
from sys import exit


def validate_input_file(file_name: str) -> str:
    """
    Read the Input File, Validate (non-blank) data, and return str contents.

    Parameters:
    - file_name (str): The Name of the Input File.

    Returns:
    str - The String Contents of the Input File.

    Raises:
    SystemExit - If the File does not exist, or is empty or blank, or read failed.
    """
    file_path = Path(file_name)
    if not file_path.exists():
        exit("The Input File does not Exist.")
    try:
        data = file_path.read_text()
    except IOError:
        exit("Failed to Read from File.")
    if validate_name(data):
        return data
    exit("Input was Empty")


def validate_name(argument) -> bool:
    """
    Determine whether an argument is a non-empty string.
        Does not count whitespace.
        Uses the strip method to remove empty space.

    Parameters:
    - argument (str) : The given argument.

    Returns:
    bool - True if the argument qualifies as valid.
    """
    if argument is None or not isinstance(argument, str):
        return False
    elif len(argument.strip()) < 1:
        return False
    return True
