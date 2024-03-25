"""Commit Text Organizer Package"""
from text.commit_text_organizer import CommitTextOrganizer


def process_with_cto(input_text: str) -> str:
	"""Process the Input Text with Commit Text Organizer
	"""
    cto = CommitTextOrganizer()
    cto.receive_data(input_data)
    cto.autoprocess() # Default Processing Operations
    return cto.output_all_groups()
