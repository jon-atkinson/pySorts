import sorts
import gen_data_sets
import timeit
import os
import ctypes
# import seaborn as sns
# import tk

def compare_sort_algos(command_args):
    verbose = '-v' in command_args or '--verbose' in command_args
    pretty = '-p' in command_args or '--pretty' in command_args

    in_strs = input("Enter algorithm(s) (single line, split on spaces, default all configured): ").strip().split()
    if in_strs == []:
        in_strs = ["bct", "bub", "cnt", "hep", "ins", "mrg", "qck", "rdx", "sel", "shl", "tim", "bubC", "hepC", "insC", "selC"]
    elif in_strs[0] == 'q':
        return None

    n_str = input("Enter n (default 10 000): ").strip()
    if n_str == 'q' or n_str == 'quit':
        return None
    if n_str == '':
        n = 10000
    else:
        n = int(n_str)

    arr_type = input("Enter input sortedness (default 'rand'): ").strip()
    if arr_type == 'q' or n_str == 'quit':
        return None
    if arr_type == '':
        arr_type = 'rand'

    num_reps_str = input("Enter number of repetitions (default 1): ").strip()
    if num_reps_str == 'q' or n_str == 'quit':
        return None
    if num_reps_str == '':
        num_reps = 1
    else:
        num_reps = int(num_reps_str)

    algos = []
    for in_str in in_strs:
        algos.append(get_algo(in_str))
    if (None in algos):
        raise Exception("Error: an algo didn't populate correctly")

    results = compute_algo_comparisons(algos, in_strs, n, arr_type, num_reps, verbose)
    if pretty:
        unit = min(results.values())
        for elem in results.keys():
            print(elem + '\t\t' + '#' * int(results[elem] / unit) + f"\t({round(results[elem] / unit, 2)} * {[k for k, v in results.items() if v == unit][0]})")
    else:
        for elem in results.keys():
            print(elem + "\t\t" + str(results[elem]))
    return


    """ compares the average runtimes of different algorithms on on type of input
    algos: list of refs to algorithms to compare
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
        # new input array since repeating one allows python memory cache optimisations
        arr = get_arr(arr_type)(n, "python")

        if arr is None:
            print('error in input array type')
            return None

        if not verbose:
            for j, elem in enumerate(in_strs):
                if (elem[len(elem) - 1] == "C"):
                    results[elem] += timeit.timeit(lambda: algos[j](gen_data_sets.to_c_arr(deep_array_copy(arr), n), n), number=1)
                else:
                    results[elem] += timeit.timeit(lambda: algos[j](deep_array_copy(arr), n), number=1)
        else: # TODO refactor eventually, this is quite an inelegant and inefficient soln. to this problem
            print('(running in verbose mode)')
            for j, elem in enumerate(in_strs):
                if (elem[-1] == "C"):
                    inArray = gen_data_sets.to_c_arr(deep_array_copy(arr), n)
                    sortedArray = algos[j](inArray, n)
                else:
                    sortedArray = algos[j](deep_array_copy(arr), n)

                print("\n\n(" + elem + ")\nInitial: " + str(arr[0:n]) + "\nFinal: " + str(sortedArray[0:n]), end="")

                if (elem[-1] == "C"):
                    results[elem] += timeit.timeit(lambda: algos[j](gen_data_sets.to_c_arr(deep_array_copy(arr), n), n), number=1)
                else:
                    results[elem] += timeit.timeit(lambda: algos[j](deep_array_copy(arr), n), number=1)


    # meaningless for comparison since #reps introduces a constant scale factor but for semantic sakes
    # also helps when considering rough runtimes over tests with different number of repeat tests
    print()
    for i, elem in enumerate(in_strs):
        results[elem] /= num_reps
    return results


    """Compares the average runtimes of one algorithm on inputs of different
    sortedness
    """
def compare_sortedness(verbose):
    print("TODO: implement compare_sortedness")
    return


    """ Plots the O(n) response of multiple algorithms on one input type
    algos: list of refs to algorithms to compare
    in_strs: list of strings corresponding to the algos being compared
    n: size of array being sorted
    arr_type: string representing the sortedness of the array
    num_reps: number of reps (with newly gen arrs per rep) to be avged
    """
def plot_algos(command_args):
    print("TODO - implement this operation")
    return


    """ takes a string refering to the desired algorithm
    returns a reference to the function of the desired algorithm
    """
def get_algo(inStr):
    # importing and loading cSorts lib
    script_dir = os.path.abspath(os.path.dirname(__file__))
    lib_path = os.path.join(script_dir, "../c/cSorts.so")
    cSorts = ctypes.cdll.LoadLibrary(lib_path)
    
    match inStr:
        case "bct":
            return sorts.bucket_sort
        case "bctC":
            return construct_c_algo(cSorts.bucketSort)
        case "bub":
            return sorts.bubble_sort
        case "bubC":
            return construct_c_algo(cSorts.bubbleSort)
        case "cnt":
            return sorts.count_sort
        case "cntC":
            return construct_c_algo(cSorts.countSort)
        case "hep":
            return sorts.heap_sort
        case "hepC":
            return construct_c_algo(cSorts.heapSort)
        case "ins":
            return sorts.insertion_sort
        case "insC":
            return construct_c_algo(cSorts.insertionSort)
        case "mrg":
            return sorts.merge_sort
        case "mrgC":
            return construct_c_algo(cSorts.mergeSort)
        case "qck":
            return sorts.quick_sort
        case "qckC":
            return construct_c_algo(cSorts.quickSort)
        case "rdx":
            return sorts.radix_sort
        case "rdxC":
            return construct_c_algo(cSorts.radixSort)
        case "sel":
            return sorts.selection_sort
        case "selC":
            return construct_c_algo(cSorts.selectionSort)
        case "shl":
            return sorts.shell_sort
        case "shlC":
            return construct_c_algo(cSorts.shellSort)
        case "tim":
            return sorts.tim_sort
        case "timC":
            return construct_c_algo(cSorts.timSort)
        case "tre":
            return sorts.tree_sort
        case "treC":
            return construct_c_algo(cSorts.treeSort)
        case _:
            print("No matching algorithm found")
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
        case "norm":
            return gen_data_sets.gen_norm_rand_arr
        case "posSkew":
            return gen_data_sets.gen_pos_skew_arr
        case "negSkew":
            return gen_data_sets.gen_neg_skew_arr
        case _:
            return None

def deep_array_copy(arr):
    new = []
    for e in arr:
        new.append(e)
    return new

if __name__ == "__main__":
    import cli
    os.system('clear')
    print("Running from operation.py")
    cli.commandLoop()
