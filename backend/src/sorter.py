import time
from typing import List, Tuple

import src.arrays as arrays
import src.backend_config as config


def call(algorithm: str, language: str, array: List[int]) -> Tuple[List[int], float]:
    """
    Execute the specified algorithm in the given language on the input array.

    Args:
        algorithm (str): Name of the algorithm.
        language (str): Language in which the algorithm is implemented.
        array (List[int]): The input array to sort.
        time_execution (bool): Whether to return execution time.

    Returns:
        Tuple[List[int], float]: The sorted array and the execution time.
    """
    if (
        language not in config.algorithms.keys()
        or language not in arrays.language_converters.keys()
    ):
        raise ValueError(f"Unsupported language: {language}")
    if algorithm not in list(config.algorithms[language].keys()):
        raise ValueError(
            f"No implementation for {algorithm} written in {language} configured"
        )

    algorithm_impl = config.algorithms[language][algorithm]
    array = arrays.language_converters[language](array)

    start_time = time.perf_counter()
    algorithm_impl(array, len(array))
    end_time = time.perf_counter()

    return array, (end_time - start_time)
