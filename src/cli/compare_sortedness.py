import helpers as helpers
import requests
from cli_config import API_URL as API_URL


def compare_sortedness(filename: str, configuration: dict):
    """
    Sends a POST request to the compare-sortedness API route and prints the
            formatted results to terminal.

    Args:
        filename (str): file containing the query
        configuration (dict): json config of the backend API
    """
    try:
        algorithm, low, high, arr_types, num_reps, step = parse_cla(
            filename, configuration
        )

        request_body = {
            "algorithm": algorithm,
            "low": low,
            "high": high,
            "arr_types": arr_types,
            "num_reps": num_reps,
            "step": step,
        }

        response = requests.post(API_URL + "/compare-sortedness", json=request_body)

        if response.status_code == 200:
            results = response.json()
            print("Results:")
            for sortedness, series in results:
                print(f"Sortedness: {sortedness}")
                for length, avg_time in series:
                    print(f"  Input Length: {length}, Average Time: {avg_time}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error processing command: {str(e)}")


def parse_cla(filename: str, configuration: dict):
    """
    Parse and validate the JSON file provided as a command-line argument using
            provided configuration

    Args:
        command_args (str): Path to the JSON configuration file.
        backend_config (dict): Backend configuration for validation.

    Returns:
        tuple: Parse and validated configuration values
    """
    request = helpers.read_and_decode_file(filename)

    request_well_formed(request)
    request_values_valid(request, configuration)

    algorithm = request["algorithm"]
    low = request["low"]
    high = request["high"]
    arr_types = request["array types"]
    num_reps = request["number repetitions"]
    step = request["step"]

    return algorithm, low, high, arr_types, num_reps, step


def request_well_formed(request: dict):
    """
    Checks that the compare algorithms request is well-formed and contains all
            required keys with values of the correct types.

    Args:
        request (dict): The request dictionary containing comparison parameters
                and algorithms.
            Required keys include "algorithm", "low", "high", "array types",
                    "nuymber repetitions", and "step".

    Raises:
        ValueError: If required keys are missing, if the 'algorithms' key is not
                a list of dictionaries with 'algorithm' and 'language' keys, if
                numeric values are not integers, or if 'array type' is not a string.
    """
    required_keys = [
        "algorithm",
        "low",
        "high",
        "array types",
        "number repetitions",
        "step",
    ]
    missing_keys = [key for key in required_keys if key not in request]
    if missing_keys:
        raise ValueError(f"Missing required keys in request: {', '.join(missing_keys)}")

    array_types = request.get("array types", [])
    if not isinstance(array_types, list) or not all(
        isinstance(entry, str) for entry in array_types
    ):
        raise ValueError("Invalid 'array types' format. Each entry must be a string.")

    low = request["low"]
    high = request["high"]
    num_reps = request["number repetitions"]
    step = request["step"]
    if not (
        isinstance(low, int)
        and isinstance(high, int)
        and isinstance(num_reps, int)
        and isinstance(step, int)
    ):
        raise ValueError(
            "'low', 'high', 'number repetitions', and 'step' must all be integers."
        )

    algorithm = request["algorithm"]
    if (
        not isinstance(algorithm, dict)
        or "algorithm" not in algorithm
        or "language" not in algorithm
    ):
        raise ValueError(
            "'algorithm' must be a dict with keys 'algorithm' and 'language'."
        )


def request_values_valid(request: dict, configuration: dict):
    """
    Validates that he values in the compare sortedness request are within the
    expected ranges and theat the algorithm specified have corresponding
    implementations in the configuration.

    Args:
        request (dict): The request dictionary containing comparison parameters
                and array types.
            Expected keys include "low", "high", "number repetitions", "step",
                    "algorithm", and "array types".

    Raises:
        ValueError: If 'low' is not less than 'high', if 'number repetitions' or
                'step' are not positive integers, or if any specified algorithm
                or input type does not have a configured implementation.
    """
    low = request["low"]
    high = request["high"]
    num_reps = request["number repetitions"]
    step = request["step"]
    algorithm = request["algorithm"]
    array_types = request["array types"]
    if low >= high:
        raise ValueError("'low' must be less than 'high'.")
    if num_reps <= 0 or step <= 0:
        raise ValueError("'number repetitions' and 'step' must be positive integers.")
    if algorithm["language"] not in configuration["algorithms"].keys():
        language = algorithm["language"]
        raise ValueError(
            f"No implementation for '{algorithm}' in '{language}' configured."
        )

    for array_type in array_types:
        if array_type not in configuration["array types"]:
            raise ValueError(f"'{array_type}' input type not configured.")
