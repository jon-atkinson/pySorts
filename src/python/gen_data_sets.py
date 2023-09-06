import random
import time
import ctypes

def gen_rand_arr(n, language):
    arr = []
    random.seed(time.time())
    for _ in range(n):
        arr.append(random.randint(0, n))
    return parse_arr_type(arr, n, language)

def gen_pos_skew_arr(n, language):
    print("TODO")
    return None

def gen_neg_skew_arr(n, language):
    print("TODO")
    return None

def gen_many_rep_arr(n, language):
    arr = []
    random.seed(time.time())
    for _ in range(n):
        arr.append(random.randint(0, n / 10))
    return parse_arr_type(arr, n, language)

def gen_pre_sorted_arr(n, language):
    arr = []
    for i in range(n):
        arr.append(i)
    return parse_arr_type(arr, n, language)

def gen_rev_sorted_arr(n, language):
    arr = []
    for i in range(n):
        arr.append(n - i - 1)
    return parse_arr_type(arr, n, language)

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
    return (ctypes.c_int * n)(*arr)

if __name__ == "__main__":
    # import sorts
    import operation
    # print(sorts.selection_sort(gen_rand_arr(100, "python"), 100))
    n = 10
    arr = []
    for i in [0,1,2,3,4,5,6,7,8,9]:
        arr.append(i)
    print(arr)
    newArr = to_c_arr(operation.deep_array_copy(arr), n)
    print(newArr)
    print("reminder, the above two c array objects should be identical")
    for j in [0,1,2,3,4,5,6,7,8,9]:
        print(newArr[j], ' ', end='')
