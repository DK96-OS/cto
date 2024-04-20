"""Commit Text Organizer Package
"""
from commit_text_organizer.commit_text_organizer import CommitTextOrganizer


def process_with_cto(input_text: str) -> str:
    """Process the Input Text with Commit Text Organizer
    """
    cto = CommitTextOrganizer()
    cto.receive_data(input_text)
    cto.autoprocess() # Default Processing Operations
    return cto.output_all_groups()
