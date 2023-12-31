""" Function definitions for file management """


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
