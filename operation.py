import sorts
import genDataSets
import timeit

def time_sort_algo():
    print("Enter Algorithm: ", end = "")
    in_str = input().strip()
    algo = get_algo(in_str)
    print("Enter n: ", end = "")
    n = int(input())
    print("Enter input sortedness: ", end = "")
    arr = get_arr(input().strip(), n)
    if (algo == None or arr == None):
        print("Error: algo or arr didn't populate correctly")
        return None
    print(in_str + "\t\t" + str(timeit.timeit(lambda: algo(arr), number=1)))
    

def race_sort_algos():
    print("Enter Algorithms (single line, split on spaces): ", end = "")
    in_strs = input().strip().split()
    print("Enter n: ", end = "")
    n = int(input())
    print("Enter input sortedness: ", end = "")
    arr = get_arr(input().strip(), n)
    algos = []
    for in_str in in_strs:
        algos.append(get_algo(in_str))
    if (None in algos):
        print("Error: an algo or arr didn't populate correctly")
        return None
    for i in range(len(algos)):
        print(in_strs[i] + "\t\t" + str(timeit.timeit(lambda: algos[i](arr), number=1)))
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
