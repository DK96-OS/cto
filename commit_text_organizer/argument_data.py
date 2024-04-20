"""The Arguments Received from the Command Line Input.

This DataClass is created after the argument syntax is validated.

Syntax Validation:
- The Input File is Present and non-blank.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ArgumentData:
    """
    The arguments received by Argument Parser.

    Properties:
    - input_file_name (str): The Name of the File containing the input.
    """

    input_file_name: str
