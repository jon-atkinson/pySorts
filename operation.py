import sorts
import gen_data_sets as gen_data_sets
import timeit
import os
import seaborn as sns
import ctypes
import tk

def compare_sort_algos(command_args):
    verbose = '-v' in command_args or '--verbose' in command_args
    pretty = '-p' in command_args or '--pretty' in command_args

    in_strs = input("Enter algorithm(s) (single line, split on spaces): ").strip().split()
    if in_strs[0] == 'q':
        return None

    n_str = input("Enter n (default 10 000): ")
    if n_str == 'q':
        return None
    if n_str == '':
        n = 10000
    else:
        n = int(n_str)

    arr_type = input("Enter input sortedness (default 'rand'): ").strip()
    if arr_type == 'q':
        return None
    if arr_type == '':
        arr_type = 'rand'

    num_reps_str = input("Enter number of repetitions (default 1): ")
    if num_reps_str == 'q':
        return None
    if num_reps_str == '':
        num_reps = 1
    else:
        num_reps = int(num_reps_str)

    algos = []
    for in_str in in_strs:
        algos.append(get_algo(in_str))
    if (None in algos):
        print("Error: an algo didn't populate correctly")
        return None
    else:
        for algo in algos:
            print(algo)

    results = compute_algo_comparisons(algos, in_strs, n, arr_type, num_reps, verbose)
    if pretty:
        unit = min(results.values())
        for elem in results.keys():
            print(elem + '\t\t' + '#' * int(results[elem]/unit))
    else:
        for elem in results.keys():
            print(elem + "\t\t" + str(results[elem]))
    return


    """algos: list of refs to algorithms to compare
    in_strs: list of strings corresponding to the algos being compared
    n: size of array being sorted
    arr_type: string representing the sortedness of the array
    num_reps: number of reps (with newly gen arrs per rep) to be avged
    """
def compute_algo_comparisons(algos, in_strs, n, arr_type, num_reps, verbose):
    results = dict()
    for i, elem in enumerate(in_strs):
        results.update({in_strs[i]: 0.0})

    for i in range(num_reps):
        # new input array since repeating one allows for python memory reuse optimisation interferance
        arr = get_arr(arr_type)(n, "python")
        c_arr = gen_data_sets.to_c_arr(arr, n)

        if arr == None:
            print('error in input array type')
            return None

        if not verbose:
            for j, elem in enumerate(in_strs):
                if (elem[len(elem) - 1] == "C"):
                    results[elem] += timeit.timeit(lambda: algos[j](c_arr, n), number=1)
                else:
                    results[elem] += timeit.timeit(lambda: algos[j](arr, n), number=1)
        else: # TODO delete eventually, this is quite an inelegant and inefficient soln. to this problem
            print('(running in verbose mode)')
            for j, elem in enumerate(in_strs):
                sortedArray = algos[j](arr, n)
                for i in range(n):
                    print(sortedArray[i], "", end="")
                results[elem] += timeit.timeit(lambda: algos[j](arr, n), number=1)

    # meaningless for comparison since #reps introduces a constant scale factor but for semantic sakes
    for i, elem in enumerate(in_strs):
        results[elem] /= num_reps
    return results

def compare_sortedness(verbose):
    print("TODO: implement compare_sortedness")
    return

def plot_algos(command_args):
    print("TODO - implement this operation")
    return


    """ takes a string refering to the desired algorithm
    returns a reference to the function of the desired algorithm
    """
def get_algo(inStr):
    # importing cSorts lib
    script_dir = os.path.abspath(os.path.dirname(__file__))
    lib_path = os.path.join(script_dir, "cSorts.so")
    cSorts = ctypes.cdll.LoadLibrary(lib_path)
    
    match inStr:
        case "sel":
            return sorts.selection_sort
        case "selC":
            return construct_c_algo(cSorts.selectionSort)
        case "bub":
            return sorts.bubble_sort
        case "bubC":
            bubbleSort = cSorts.bubbleSort
            bubbleSort.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
            bubbleSort.restype = ctypes.POINTER(ctypes.c_int)
            return bubbleSort
        case "ins":
            return sorts.insertion_sort
        case "hep":
            return sorts.heap_sort
        case "qck":
            return sorts.quick_sort
        case "mrg":
            return sorts.merge_sort
        case "bct":
            return sorts.bucket_sort
        case "rdx":
            return sorts.radix_sort
        case "cnt":
            return sorts.count_sort
        case "shl":
            return sorts.shell_sort
        case "tim":
            return sorts.tim_sort
        case "tre":
            return sorts.tree_sort
        case "cbe":
            return sorts.cube_sort
        case _:
            return None
    
def construct_c_algo(algo_ref):
    algo_ref.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    algo_ref.restype = ctypes.POINTER(ctypes.c_int)
    return algo_ref


    """ inStr refers to the type of sortedness of the returned array
    n is the length of the returned array
    returns an array of n integers with the input sortedness
    """
def get_arr(inStr):
    match inStr:
        case "sorted":
            return gen_data_sets.gen_pre_sorted_arr
        case "reverse":
            return gen_data_sets.gen_rev_sorted_arr
        case "rand":
            return gen_data_sets.gen_rand_arr
        case "manyRep":
            return gen_data_sets.gen_many_rep_arr
        case "posSkew":
            return gen_data_sets.gen_pos_skew_arr
        case "negSkew":
            return gen_data_sets.gen_neg_skew_arr
        case _:
            return None

if __name__ == "__main__":
    import app
    print("Running from operation.py")
    app.commandLoop()