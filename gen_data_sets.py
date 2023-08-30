import random
import time
import ctypes

def gen_rand_arr(size):
    arr = []
    random.seed(time.time())
    for num in range(size):
        arr.append(random.randint(0,size))

    # c sorts require a special array type, hence the wrapper fn
    # either we extend the feature set of all generation algos to
    # return either type per user request or we standardise algo language
    return to_c_arr(arr, size)
    # return arr

def gen_pos_skew_arr(size):
    print("TODO")
    return []

def gen_neg_skew_arr(size):
    print("TODO")
    return []

def gen_many_rep_arr(size):
    array = []
    random.seed(time.time())
    for num in range(size):
        array.append(random.randint(0,size / 10))
    return array

def gen_pre_sorted_arr(size):
    arr = []
    for i in range(size):
        arr.append(i)
    return arr

def gen_rev_sorted_arr(size):
    arr = []
    for i in range(size):
        arr.append(size - i)
    return arr
    
if __name__ == "__main__":
    import sorts
    print(sorts.selection_sort(gen_many_rep_arr(100), 1))

def to_c_arr(arr, n):
    arr_c = (ctypes.c_int * n)(*arr)
    print(arr)
    print(arr_c)
    return arr_c