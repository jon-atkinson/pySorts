import random
import time

def gen_rand_arr(size):
    arr = []
    random.seed(time.time())
    for num in range(size):
        arr.append(random.randint(0,size))
    return arr

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
