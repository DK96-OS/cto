""" Function definitions for file management """


def create_new_file_name(
        file_name: str,
        suffix: str
) -> str:
    """ Create a new file name with a suffix.
    """
    if file_name.endswith('.txt'):
        return f"{file_name[:-4]}{suffix}.txt"
    else:
        return f"{file_name}{suffix}"


def read_file(
		name: str
) -> str | None:
	""" Open and read a file to a string.
	"""
	try:
		with open(
				file=name,
				mode='rt'
		) as f:
			return f.read()
	except OSError:
		return None


def write_file(
		name: str,
		data: str
):
	""" Write string data to a file.
	"""
	try:
		with open(
				file=name,
				mode='w'
		) as f:
			f.write(data)
		return True
	except OSError:
		return False
