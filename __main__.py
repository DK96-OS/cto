#!usr/bin/python3
from pathlib import Path
from sys import argv

from text.commit_text_organizer import CommitTextOrganizer
from files.file_management import read_file, write_file, create_new_file_name


def main():
    input_file = argv[1:][0] # Filename
    output_file = create_new_file_name(input_file, "-org")
    # Load the Input File
    if (input_data := read_file(input_file)) is None:
        exit('Failed to Read Input File')
    # Process with CTO
    org = CommitTextOrganizer()
    org.receive_data(input_data)
    org.autoprocess() # Default Processing Operations
    output_data = org.output_all_groups()
    # Write the Result to the File
    write_file(output_file, output_data)


if __name__ == "__main__":
    # Get the directory of the current file
    # __file__ is the path to the script being executed
    current_directory = Path(__file__).resolve().parent
    # Add the directory to sys.path
    from sys import path
    path.append(str(current_directory))
    main()
