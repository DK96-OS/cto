"""For Loading Sample Data from Files.
"""
from pathlib import Path


def _read_file(
		name: str
) -> str:
	""" Open and read a file to a string.
	"""
	try:
		file_path = Path(name)
		if not file_path.exists():
			exit('File Does not Exist')
		return file_path.read_text()
	except IOError:
		return ""
