"""Valid Input Data Class.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class InputData:
    """A Data Class Containing Program Input.

    Properties:
    - text_input (str): The Input text to the CTO operation.
    """
    text_input: str
