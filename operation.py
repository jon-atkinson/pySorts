import sorts
import genDataSets
import timeit

# def time_sort_algo():
#     print("Enter Algorithm: ", end = "")
#     in_str = input().strip()
#     algo = get_algo(in_str)
#     print("Enter n: ", end = "")
#     n = int(input())
#     print("Enter input sortedness: ", end = "")
#     arr = get_arr(input().strip(), n)
#     if (algo == None or arr == None):
#         print("Error: algo or arr didn't populate correctly")
#         return None
#     print(in_str + "\t\t" + str(timeit.timeit(lambda: algo(arr), number=1)))
    

def compare_sort_algos():
    in_strs = input("Enter algorithm(s) (single line, split on spaces): ").strip().split()
    n = int(input("Enter n: "))
    arr_type = input("Enter input sortedness: ").strip()
    num_reps = int(input("Enter number of repetitions: "))

    algos = []
    for in_str in in_strs:
        algos.append(get_algo(in_str))
    if (None in algos):
        print("Error: an algo or arr didn't populate correctly")
        return None

    results = compute_algo_comparisons(algos, in_strs, n, arr_type, num_reps)
    for elem in results.keys():
        print(elem + "\t\t" + str(results[elem]))
    return

def compute_algo_comparisons(algos, in_strs, n, arr_type, num_reps):
    results = dict()
    for i, elem in enumerate(in_strs):
        results.update({in_strs[i]: 0.0})

    for i in range(num_reps):
        # new array since repeating one allows for python memory reuse optimisation interferance
        arr = get_arr(arr_type, n)
        for j, elem in enumerate(in_strs):
            results[elem] += timeit.timeit(lambda: algos[j](arr, n), number=1)
        
    # meaningless for comparison since scale factor but for semantic's sakes
    for i, elem in enumerate(in_strs):
        results[elem] /= num_reps  
    return results

def compare_sortedness():
    print("TODO: implement compare_sortedness")
    return

def plot_sort_algos():
    print("TODO - implement this operation")
    return


    """ takes a string refering to the desired algorithm
    returns a reference to the function of the desired algorithm
    """
def get_algo(inStr):
    match inStr:
        case "sel":
            return sorts.selection_sort
        case "bub":
            return sorts.bubble_sort
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
    

    """ inStr refers to the type of sortedness of the returned array
    n is the length of the returned array
    returns an array of n integers with the input sortedness
    """
def get_arr(inStr, n):
    match inStr:
        case "sorted":
            return genDataSets.gen_pre_sorted_arr(n)
        case "reverse":
            return genDataSets.gen_rev_sorted_arr(n)
        case "rand":
            return genDataSets.gen_rand_arr(n)
        case "manyRep":
            return genDataSets.gen_many_rep_arr(n)
        case "posSkew":
            return genDataSets.gen_pos_skew_arr(n)
        case "negSkew":
            return genDataSets.gen_neg_skew_arr(n)
        case _:
            return None
