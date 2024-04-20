#!usr/bin/python3
from pathlib import Path
from sys import argv

from commit_text_organizer.argument_parser import validate_input
from commit_text_organizer import process_with_cto


def main():
    input_data = validate_input(argv[1:])
    output_data = process_with_cto(input_data)
    if output_data is None or len(output_data) == 0:
        exit("CTO returned zero Text!")
    print(output_data)


if __name__ == "__main__":
    # Get the directory of the current file
    # __file__ is the path to the script being executed
    current_directory = Path(__file__).resolve().parent
    # Add the directory to sys.path
    from sys import path
    path.append(str(current_directory))
    main()
