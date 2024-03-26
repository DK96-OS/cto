""" Function definitions for file management """
from pathlib import Path


def read_file(
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


def write_file(
		name: str,
		data: str
) -> bool:
	""" Write string data to a file.
	"""
	if len(data) < 1:
		return False
	try:
		file_path = Path(name)
		file_path.write_text(data)
		return True
	except IOError:
		return False
