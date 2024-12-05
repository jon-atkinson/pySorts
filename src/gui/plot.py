from gui.gui_config import API_URL
import requests
from typing import List, Dict, Tuple


def plot_sortedness_gui(algorithm, start, stop, step, arr_types, num_reps):
    """ Calculates the O(n) response of one algorithms on multiple input types
    algo_str: string corresponding to the algo being evaluated
    start, stop, step: start and stop for the sweep and step = granularity
    arr_types: list of strings representing the sortedness of the arrays
    num_reps: number of reps (with newly gen arrs per rep) to be avged
    """
    data = {
        "algorithm": algorithm,
        "low": start,
        "high": stop,
        "arr_types": arr_types,
        "num_reps": num_reps,
        "step": step
    }

    try: 
        response = requests.post(API_URL + "/compare-sortedness", json=data)
        response.raise_for_status()
        result_data = response.json()

        results = {}
        n_steps = []

        for sortedness, series in result_data:
            results[sortedness] = [x[1] for x in series]
            n_steps = [x[0] for x in series]

        return n_steps, results

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while calling the API: {e}")
        return None

def plot_algos_gui(algorithms: dict, start: int, stop: int, step: int, arr_type: str, num_reps: int) -> Tuple[List[int],Dict[str,List[int]]]:
    """
    Requests API for time series comparison of the requested algorithms

    Args:
        algorithms (dict): language-algorithm pairs to be compared
        start (int): low value for input length
        stop (int): high value for input length
        step (int): increment between each input length
        arr_type (str): sortedness of the input
        num_reps (int): number of times to repeat each input length

    Returns:
        Tuple[List[int],Dict[str,List[int]]]: x-values, labelled algorithm time series
    """

    data = {
        "algorithms": algorithms,
        "low": start,
        "high": stop,
        "arr_type": arr_type,
        "num_reps": num_reps,
        "step": step
    }

    try: 
        response = requests.post(API_URL + "/compare-algorithms", json=data)
        response.raise_for_status()
        result_data = response.json()

        results = {}
        n_steps = []

        for algorithm, language, series in result_data:
            results[f"{algorithm} ({language})"] = [x[1] for x in series]
            n_steps = [x[0] for x in series]

        return n_steps, results

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while calling the API: {e}")
        return None
