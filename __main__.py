#!usr/bin/python3
from pathlib import Path
from sys import argv

from files.file_management import read_file, write_file, create_new_file_name
from text import process_with_cto


def main():
    input_file = argv[1:][0] # Filename
    output_file = create_new_file_name(input_file, "-org")
    # Load the Input File
    if (input_data := read_file(input_file)) is None:
        exit('Failed to Read Input File')
   	output_data = process_with_cto(input_data)
   	# If output is empty, prevent file write
   	if output_data is None or len(output_data) == 0:
   		exit("CTO returned zero Text!")
    write_file(output_file, output_data)


if __name__ == "__main__":
    # Get the directory of the current file
    # __file__ is the path to the script being executed
    current_directory = Path(__file__).resolve().parent
    # Add the directory to sys.path
    from sys import path
    path.append(str(current_directory))
    main()
