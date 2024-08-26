"""Defines and Validates Argument Syntax.

Encapsulates Argument Parser.

Returns Argument Data, the args provided by the User.
"""
from argparse import ArgumentParser
from sys import exit
from typing import Optional

from .argument_data import ArgumentData
from .input_data import InputData
from .file_validation import validate_input_file, validate_name


def validate_input(arguments: Optional[list[str]] = None) -> InputData:
    """
    Parse command line arguments.

    Parameters:
    - args: A list of argument strings.

    Returns:
    InputData : Container for Valid Argument Data.
    """
    if arguments is None or len(arguments) == 0:
        exit("No Arguments given.")
    # Initialize the Parser and Parse Immediately
    try:
        parsed_args = _define_arguments().parse_args(arguments)
    except SystemExit:
        exit("Unable to Parse Arguments.")
    # Validate the Arguments
    argument_data = _validate_arguments(
        parsed_args.input_file_name,
    )
    return InputData(
        validate_input_file(
        	argument_data.input_file_name
        )
    )


def _validate_arguments(
    input_file_name: str,
) -> ArgumentData:
    """
    Checks the values received from the ArgParser.
        Uses String Validation to Validate each Name.

    Parameters:
    - input_file_name (str): The file name containing the input.

    Returns:
    ArgumentData - A DataClass of syntactically correct arguments.
    """
    if not validate_name(input_file_name):
        exit("The File argument was invalid.")
    return ArgumentData(
        input_file_name,
    )


def _define_arguments() -> ArgumentParser:
    """
    Initializes and Defines Argument Parser.
       - Sets Required/Optional Arguments and Flags.

    Returns:
    argparse.ArgumentParser - An instance with all supported Arguments.
    """
    parser = ArgumentParser(
        description="Commit Text Organizer"
    )
    # Required argument
    parser.add_argument(
        'input_file_name',
        type=str,
        help='The File containing the input text.'
    )
    return parser
