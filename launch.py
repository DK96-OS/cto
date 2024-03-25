#!/usr/bin/python3
from sys import exit

from commit_organizer import CommitTextOrganizer
from files.file_management import read_file, write_file, create_new_file_name


def run_commit_text_organizer(
        input_file: str,
        output_file: str
):
    """ To Run requires in and out file paths.
    """
    # Create an instance of the CTO data structure
    org = CommitTextOrganizer()
    # Load the Input File
    if (input_data := read_file(input_file)) is None:
        exit('Failed to Read Input File')
    org.receive_data(input_data)
    # Default Processing Operations
    org.autoprocess()
    # Return all Groups of Text
    output_data = org.output_all_groups()
    # Write the Result to the File
    write_file(output_file, output_data)


# Request keyboard input
in_file = input("Input File Name:")

# If no file is given, exit
if len(in_file) < 1:
    exit()
else:
    out_file = create_new_file_name(in_file, "-org")
    # Run the CTO
    run_commit_text_organizer(in_file, out_file)
