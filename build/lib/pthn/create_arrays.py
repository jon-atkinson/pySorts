import ctypes
import numpy as np


def gen_rand_arr(n, language):
    return parse_arr_type(np.random.randint(0, n, n), n, language)


def gen_norm_rand_arr(n, language):
    return parse_arr_type(np.random.normal(loc=n/2,scale=1,size=n).astype(int), n, language)


# TODO finish implementation
def gen_pos_skew_arr(n, language):
    print("TODO")
    return None


# TODO finish implementation
def gen_neg_skew_arr(n, language):
    print("TODO")
    return None


def gen_many_rep_arr(n, language):
    return parse_arr_type(np.random.randint(0, n, n // 10), n, language)


def gen_pre_sorted_arr(n, language):
    return parse_arr_type(np.arange(0,n), n, language)


def gen_rev_sorted_arr(n, language):
    return parse_arr_type(np.arange(n,0,-1), n, language)


def parse_arr_type(arr, n, language):
    if (language == "python"):
        return arr
    elif (language == "c"):
        return to_c_arr(arr, n)
    print("Error, language param not passed in correctly")
    return None


def to_c_arr(arr, n):
    var = (ctypes.c_int * n)(*arr)
    return var
    # return (ctypes.c_int * n)(*arr)


if __name__ == "__main__":
    import operation
    n = 10
    arr = []
    for i in range(n):
        arr.append(i)
    print(arr)
    newArr = to_c_arr(operation.deep_array_copy(arr), n)
    print(newArr)
    print("reminder, the above two c array objects should be identical")
    for j in range(n):
        print(newArr[j], ' ', end='')
