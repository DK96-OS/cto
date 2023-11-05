#!/usr/bin/python3

from commit_organizer import CommitTextOrganizer
from files.file_names import create_new_file_name


def run_commit_text_organizer(
        input_file: str,
        output_file: str
):
    """ To Run requires in and out file paths.
    """
    # Create an instance of the CTO data structure
    org = CommitTextOrganizer()
    # Load the Input File
    org.read_file(input_file)
    # Default Processing Operations
    org.autoprocess()
    # Write the Result to a File
    org.write_to_file(output_file)


# Request keyboard input
in_file = input("Input File Name:")

# If no file is given, exit
if len(in_file) < 1:
    exit()
else:
    out_file = create_new_file_name(in_file, "-org")
    # Run the CTO
    run_commit_text_organizer(in_file, out_file)
