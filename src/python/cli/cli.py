import json
import os

import requests

from python.config import API_URL as API_URL


def command_loop(configuration: dict):
    """
    Main command loop for the cli frontend

    Args:
        configuration (dict): Backend API configuration

    Raises:
        ValueError: invalid command or filename input
    """
    command = input(formatPrompt("operation: ")).split(" ")
    while command[0] not in ["q", "Q", "quit", "Quit"]:
        try:
            match command[0]:
                case "h":
                    helpPySort()
                case "algo":
                    # operation.compare_sort_algos(command_args)
                    if len(command) > 2:
                        raise (
                            ValueError(
                                f"algo expected single filename argument, received={command[1:]}"
                            )
                        )
                    compare_algorithms(command[1], configuration)
                case "sorting":
                    # operation.compare_sortedness(command_args)
                    compare_sortedness(command[1], configuration)
                case "clear":
                    os.system("clear")
                case _:
                    raise ValueError(
                        f'incorrect command format. Expected one of "h", "algo", "sorting", Recieved={command}'
                    )
        except ValueError as e:
            print(e)
        command = input(formatPrompt("operation: ")).split(" ")

def parse_compare_algorithms_cla(filename: str, configuration: dict):
    """
    Parse and validate the JSON file provided as a command-line argument using
            provided configuration.

    Args:
        command_args (str): Path to the JSON configuration file.
        backend_config (dict): Backend configuration for validation.

    Returns:
        tuple: Parsed and validated configuration values.
    """
    request = read_and_decode_file(filename)

    compare_algorithms_request_well_formed(request)
    compare_algorithms_request_values_valid(request, configuration)

    algorithms = request["algorithms"]
    low = request["low"]
    high = request["high"]
    arr_type = request["array type"]
    num_reps = request["number repetitions"]
    step = request["step"]

    return algorithms, low, high, arr_type, num_reps, step

def compare_algorithms_request_values_valid(request: dict, configuration: dict):
    """
    Validates that the values in the compare algorithms request are within the
    expected ranges and that the algorithms specified have corresponding
    implementations in the configuration.

    Args:
        request (dict): The request dictionary containing comparison parameters
                and algorithms.
            Expected keys include "low", "high", "number repetitions", "step",
                    and "algorithms".
        configuration (dict): The configuration dictionary specifying available
                algorithm implementations.

    Raises:
        ValueError: If 'low' is not less than 'high', if 'number repetitions' or
                'step' are not positive integers, or if any specified algorithm
                does not have a configured implementation.
    """
    low = request["low"]
    high = request["high"]
    num_reps = request["number repetitions"]
    step = request["step"]
    if low >= high:
        raise ValueError("'low' must be less than 'high'.")
    if num_reps <= 0 or step <= 0:
        raise ValueError("'number repetitions' and 'step' must be positive integers.")

    for algorithm in request["algorithms"]:
        if algorithm["language"] not in configuration["algorithms"].keys():
            language = algorithm["language"]
            raise ValueError(
                f"No implementation for '{algorithm}' in '{language}' configured."
            )

def compare_algorithms_request_well_formed(request: dict):
    """
    Checks that the compare algorithms request is well-formed and contains all
            required keys with values of the correct types.

    Args:
        request (dict): The request dictionary containing comparison parameters
                and algorithms.
            Required keys include "algorithms", "low", "high", "array type",
                    "number repetitions", and "step".

    Raises:
        ValueError: If required keys are missing, if the 'algorithms' key is not
                a list of dictionaries with 'algorithm' and 'language' keys, if
                numeric values are not integers, or if 'array type' is not a string.
    """
    required_keys = [
        "algorithms",
        "low",
        "high",
        "array type",
        "number repetitions",
        "step",
    ]
    missing_keys = [key for key in required_keys if key not in request]
    if missing_keys:
        raise ValueError(f"Missing required keys in request: {', '.join(missing_keys)}")

    algorithms = request.get("algorithms", [])
    if not isinstance(algorithms, list) or not all(
        isinstance(entry, dict) and "algorithm" in entry and "language" in entry
        for entry in algorithms
    ):
        raise ValueError(
            "Invalid 'algorithms' format. Each entry must be a dictionary with 'algorithm' and 'language' keys."
        )

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

    arr_type = request["array type"]
    if not isinstance(arr_type, str):
        raise ValueError("'array type' must be a string.")

def compare_sortedness_request_well_formed(request: dict):
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
        isinstance(entry, str)
        for entry in array_types
    ):
        raise ValueError(
            "Invalid 'array types' format. Each entry must be a string."
        )

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
    if not isinstance(algorithm, dict) or "algorithm" not in algorithm or "language" not in algorithm:
        raise ValueError("'algorithm' must be a dict with keys 'algorithm' and 'language'.")

def compare_sortedness(filename: str, configuration: dict):
    """
    Sends a POST request to the compare-sortedness API route and prints the
            formatted results to terminal.

    Args:
        filename (str): file containing the query
        configuration (dict): json config of the backend API
    """
    try:
        algorithm, low, high, arr_types, num_reps, step = parse_compare_sortedness_cla(
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
                print(f"  {sortedness}:")
                for length, avg_time in series:
                    print(f"  Input Length: {length}, Average Time: {avg_time}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error in CLI: {str(e)}")


def compare_algorithms(filename: str, configuration: dict):
    """
    Sends a POST request to the compare-algorithms API route and prints the
            formatted results to terminal.

    Args:
        filename (str): file containing the query
        configuration (_type_): json config of the backend API
    """
    try:
        algorithms, low, high, arr_type, num_reps, step = parse_compare_algorithms_cla(
            filename, configuration
        )

        request_body = {
            "algorithms": algorithms,
            "low": low,
            "high": high,
            "arr_type": arr_type,
            "num_reps": num_reps,
            "step": step,
        }

        response = requests.post(API_URL + "/compare-algorithms", json=request_body)

        if response.status_code == 200:
            results = response.json()
            print("Results:")
            for algorithm, language, series in results:
                print(f"Algorithm: {algorithm}, Language: {language}")
                for length, avg_time in series:
                    print(f"  Input Length: {length}, Average Time: {avg_time}")
        else:
            print(f"Error: {response.status_code} - {response.text}")

    except Exception as e:
        print(f"Error processing command: {str(e)}")

def parse_compare_sortedness_cla(filename: str, configuration: dict):
    request = read_and_decode_file(filename)

    compare_sortedness_request_well_formed(request)
    compare_sortedness_request_values_valid(request, configuration)

    algorithm = request["algorithm"]
    low = request["low"]
    high = request["high"]
    arr_types = request["array types"]
    num_reps = request["number repetitions"]
    step = request["step"]

    return algorithm, low, high, arr_types, num_reps, step

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

def compare_sortedness_request_values_valid(request: dict, configuration: dict):
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
            raise ValueError(
                f"'{array_type}' input type not configured."
            )

def helpPySort():
    print("Usage: algo query_filename")


def formatPrompt(promptMsg):
    return ("\033[94m {}\033[00m".format(promptMsg)).strip()


def runCLI():
    os.system("clear")
    print(formatPrompt("Welcome to pySorts, please enter a command:"))

    try:
        response = requests.get(API_URL + "/config")
        if response.status_code == 200:
            command_loop(response.json())
        else:
            print(
                f"Error fetching sorter configuration: {response.status_code} - {response.text}"
            )

    except Exception as e:
        print(f"Generic Error Caught: {str(e)}")


if __name__ == "__main__":
    runCLI()
