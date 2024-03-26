#!/usr/bin/python3
from sys import exit

from files.io import read_file, write_file
from files.names import create_new_file_name
from text import process_with_cto


def run_commit_text_organizer(
        input_file: str,
        output_file: str
):
    """ Run CTO on the Input file name

    Parameters:
    - input_file (str): The name of the file to read.
    - output_file (str): The name of the output file.
    """
    if (input_data := read_file(input_file)) is None:
        exit('Failed to Read Input File')
    output_data = process_with_cto(input_data)
   	# If output is empty, prevent file write
    if output_data is None or len(output_data) == 0:
        exit("CTO returned zero Text!")
    write_file(output_file, output_data)


# Request keyboard input
in_file = input("Input File Name:")

# If no file is given, exit
if len(in_file) < 1:
    exit('No File Received')
else:
    out_file = create_new_file_name(in_file, "-org")
    # Run the CTO
    run_commit_text_organizer(in_file, out_file)
