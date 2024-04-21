""" Important Method for use in cto_samples Tests """
import os
import unittest

from tests.cto_samples import _read_file
from commit_text_organizer.commit_organizer import CommitOrganizer


def assert_sample_expectations(
        self: unittest.TestCase,
        sample_prefix: str,
        sample_id: int
):
    # Check the Current Working Directory if it is the tests folder
    # This is a workaround for the way the UnitTest module works
    if not os.getcwd().endswith("tests"):
        os.chdir("tests")
    cto = load_new_cto(
        "cto_samples/" + sample_prefix, sample_id
    )
    cto.autoprocess()
    #
    expected_output = load_sample_output(
        "cto_samples/" + sample_prefix, sample_id
    )
    self.assertEqual(
        expected_output,
        cto.output_all_groups()
    )


def load_new_cto(
        file_prefix: str,
        sample_id: int
) -> CommitOrganizer:
    """ Load the sample with the given id from the file.
    """
    file_name = str.format(f"{file_prefix}{sample_id}.in")
    input_data = _read_file(file_name)
    if input_data is None:
        print("Tried to load: " + file_name)
        raise AssertionError(str.format(f"Sample IN #{sample_id} could Not be loaded"))
    #
    cto = CommitOrganizer()
    cto.receive_data(input_data)
    return cto


def load_sample_output(
        file_prefix: str,
        sample_id: int
) -> str:
    """ Load the sample output """
    file_name = str.format(f"{file_prefix}{sample_id}.expect")
    output_data = _read_file(file_name)
    if output_data is None:
        raise AssertionError(f"Sample OUT #{sample_id} could Not be loaded")
    return output_data
