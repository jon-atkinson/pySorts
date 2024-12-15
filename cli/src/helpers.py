import json


def read_and_decode_file(filename: str) -> dict:
    try:
        with open(filename, "r") as file:
            request = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' does not exist.")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Invalid JSON format in file '{filename}': {e}", doc=e.doc, pos=e.pos
        )
    return request

