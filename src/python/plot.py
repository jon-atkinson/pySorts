# from tkinter import *
# from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import create_arrays
import operation
import timeit

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
                    results[elem][i] += timeit.timeit(lambda: algos[j](create_arrays.to_c_arr(operation.deep_array_copy(arr), n), n), number=1) / num_reps
                else:
                    results[elem][i] += timeit.timeit(lambda: algos[j](operation.deep_array_copy(arr), n), number=1) / num_reps

        i += 1

    # plotting algorithm time response curves
    print("plotting!")
    for elem in results:
        plt.plot(n_steps, results[elem])
    plt.legend(in_strs)
    plt.title(f"Average runtimes for {num_reps} repetition(s) of each algorithm")
    plt.xlabel("Array Length (n)")
    plt.ylabel("Time Cost (s)")
    plt.show()
    return


def plot_algos_gui(in_strs, start, stop, step, arr_type, num_reps):
    """ Plots the O(n) response of multiple algorithms on one input type
    algos: list of refs to algorithms to compare
    in_strs: list of strings corresponding to the algos being compared
    start, stop, step: start and stop for the sweep and step = granularity
    arr_type: string representing the sortedness of the array
    num_reps: number of reps (with newly gen arrs per rep) to be avged
    """

    print("in_strs: ", in_strs)
    print("start: ", start)
    print("stop: ", stop)
    print("step: ", step)
    print("arr_type: ", arr_type)
    print("num_reps: ", num_reps)

    # in_strs = input("Enter algorithm(s) (single line, split on spaces, default all configured): ").strip().split()
    # if in_strs == []:
    #     in_strs = ["bct", "bub", "cnt", "hep", "ins", "mrg", "qck", "rdx", "sel", "shl", "tim", "bubC", "hepC", "insC", "selC"]
    # elif in_strs[0] == 'q':
    #     return None

    # # throws error if not 2 inputs, requires update at some point
    # inputs = input("Enter start, stop, step (optional): ").strip().split()
    # if len(inputs) == 2:
    #     start, stop = inputs
    #     step = 1
    # elif len(inputs) == 3:
    #     start, stop, step = inputs
    # else:
    #     raise Exception("invalid start, stop, step inputs")
    # start, stop, step = int(start), int(stop), int(step)

    # arr_type = input("Enter input sortedness (default 'rand'): ").strip()
    # if arr_type == 'q' or arr_type == 'quit':
    #     return None
    # if arr_type == '':
    #     arr_type = 'rand'

    # num_reps_str = input("Enter number of repetitions (default 1): ").strip()
    # if num_reps_str == 'q':
    #     return None
    # if num_reps_str == '':
    #     num_reps = 1
    # else:
    #     num_reps = int(num_reps_str)

    # algos = []
    # for in_str in in_strs:
    #     algos.append(operation.get_algo(in_str))
    # if (None in algos):
    #     raise Exception("Error: an algo didn't populate correctly")

    # results = dict()
    # for i, elem in enumerate(in_strs):
    #     results.update({in_strs[i]: []})
    # n_steps = []

    # i = 0
    # for n in range(start, stop + 1, step):
    #     n_steps.append(n)

    #     for _ in range(num_reps):
    #         # new input array since repeating one allows python memory cache optimisations
    #         arr = operation.get_arr(arr_type)(n, "python")

    #         if arr is None:
    #             print('error in input array type')
    #             return None

    #         for j, elem in enumerate(in_strs):
    #             if len(results[elem]) <= i:
    #                 results[elem].append(0)
    #             if (elem[-1] == "C"):
    #                 results[elem][i] += timeit.timeit(lambda: algos[j](create_arrays.to_c_arr(operation.deep_array_copy(arr), n), n), number=1) / num_reps
    #             else:
    #                 results[elem][i] += timeit.timeit(lambda: algos[j](operation.deep_array_copy(arr), n), number=1) / num_reps

    #     i += 1

    # # plotting algorithm time response curves
    # print("plotting!")
    # for elem in results:
    #     plt.plot(n_steps, results[elem])
    # plt.legend(in_strs)
    # plt.title(f"Average runtimes for {num_reps} repetition(s) of each algorithm")
    # plt.xlabel("Array Length (n)")
    # plt.ylabel("Time Cost (s)")
    # plt.show()
    # return