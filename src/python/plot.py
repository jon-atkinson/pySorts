import matplotlib.pyplot as plt
import python.arrays as arrays
import python.operation as operation
import timeit
from python.config import API_URL as API_URL
import requests


def plot_algos_cli(command_args):
    """ Plots the O(n) response of multiple algorithms on one input type
    algos: list of refs to algorithms to compare
    in_strs: list of strings corresponding to the algos being compared
    start, stop, step: start and stop for the sweep and step = granularity
    arr_type: string representing the sortedness of the array
    num_reps: number of reps (with newly gen arrs per rep) to be avged
    """

    in_strs = input("Enter algorithm(s) (single line, split on spaces, default all configured): ").strip().split()
    if in_strs == []:
        in_strs = ["bct", "bub", "cnt", "hep", "ins", "mrg", "qck", "rdx", "sel", "shl", "tim", "bubC", "hepC", "insC", "selC"]
    elif in_strs[0] == 'q':
        return None

    # throws error if not 2 inputs, requires update at some point
    inputs = input("Enter start, stop, step (optional): ").strip().split()
    if len(inputs) == 2:
        start, stop = inputs
        step = 1
    elif len(inputs) == 3:
        start, stop, step = inputs
    else:
        raise Exception("invalid start, stop, step inputs")
    start, stop, step = int(start), int(stop), int(step)

    arr_type = input("Enter input sortedness (default 'rand'): ").strip()
    if arr_type == 'q' or arr_type == 'quit':
        return None
    if arr_type == '':
        arr_type = 'rand'

    num_reps_str = input("Enter number of repetitions (default 1): ").strip()
    if num_reps_str == 'q':
        return None
    if num_reps_str == '':
        num_reps = 1
    else:
        num_reps = int(num_reps_str)

    algos = []
    for in_str in in_strs:
        algos.append(operation.get_algo(in_str))
    if (None in algos):
        raise Exception("Error: an algo didn't populate correctly")

    results = dict()
    for i, elem in enumerate(in_strs):
        results.update({in_strs[i]: []})
    n_steps = []

    i = 0
    for n in range(start, stop + 1, step):
        n_steps.append(n)

        for _ in range(num_reps):
            # new input array since repeating one allows python memory cache optimisations
            arr = operation.get_arr(arr_type)(n, "python")

            if arr is None:
                print('error in input array type')
                return None

            for j, elem in enumerate(in_strs):
                if len(results[elem]) <= i:
                    results[elem].append(0)
                if (elem[-1] == "C"):
                    results[elem][i] += timeit.timeit(lambda: algos[j](arrays.to_c_arr(operation.deep_array_copy(arr), n), n), number=1) / num_reps
                else:
                    results[elem][i] += timeit.timeit(lambda: algos[j](operation.deep_array_copy(arr), n), number=1) / num_reps

        i += 1

    # plotting algorithm time response curves
    for elem in results:
        plt.plot(n_steps, results[elem])
    plt.legend(in_strs)
    plt.title(f"Average runtimes for {num_reps} repetition(s) of each algorithm")
    plt.xlabel("Array Length (n)")
    plt.ylabel("Time Cost (s)")
    plt.show()
    return


def plot_sortedness_gui(algo_str, start, stop, step, arr_types, num_reps):
    """ Calculates the O(n) response of one algorithms on multiple input types
    algo_str: string corresponding to the algo being evaluated
    start, stop, step: start and stop for the sweep and step = granularity
    arr_types: list of strings representing the sortedness of the arrays
    num_reps: number of reps (with newly gen arrs per rep) to be avged
    """

    algo = operation.get_algo(algo_str)

    results = dict()
    for i in range(len(arr_types)):
        results.update({arr_types[i]: []})
    n_steps = []

    i = 0
    for n in range(start, stop + 1, step):
        n_steps.append(n)

        for _ in range(num_reps):
            for arr_type in arr_types:
                arr = operation.get_arr(arr_type)(n, "python")

                if arr is None:
                    raise Exception("array to be sorted cannot not be empty")

                if len(results[arr_type]) <= i:
                    results[arr_type].append(0)
                if (algo_str[-1] == "C"):
                    results[arr_type][i] += timeit.timeit(lambda: algo(arrays.to_c_arr(operation.deep_array_copy(arr), n), n), number=1) / num_reps
                else:
                    results[arr_type][i] += timeit.timeit(lambda: algo(operation.deep_array_copy(arr), n), number=1) / num_reps

        i += 1

    return n_steps, results


def plot_algos_gui(in_strs, start, stop, step, arr_type, num_reps):
    # """ Calculates the O(n) response of multiple algorithms on one input type
    # in_strs: list of strings corresponding to the algos being compared
    # start, stop, step: start and stop for the sweep and step = granularity
    # arr_type: string representing the sortedness of the array
    # num_reps: number of reps (with newly gen arrs per rep) to be avged
    # """

    data = {
        # "algorithms": [{"algorithm": algo, "language": "python"} for algo in in_strs],
        "algorithms": [{"algorithm": "bubble_sort", "language": "python"}],
        "low": start,
        "high": stop,
        "arr_type": arr_type,
        "num_reps": num_reps,
        "step": step
    }

    try: 
        print("attempting to call api in plot_algos_gui()")
        response = requests.post(API_URL, json=data)
        response.raise_for_status()
        result_data = response.json()
        print("successful call to api in plot_algos_gui()")

        results = dict()
        n_steps = []

        for algorithm, language, series in result_data["results"]:
            results[algorithm] = [x[1] for x in series]
            n_steps = [x[0] for x in series]

        return n_steps, results

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while calling the API: {e}")
        return None
