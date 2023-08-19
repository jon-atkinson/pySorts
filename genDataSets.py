import random
import time

def gen_rand_arr(size):
    array = []
    random.seed(time.time())
    for num in range(size):
        array.append(random.randint(0,size))
    return array

def gen_pos_skew_arr(size):
    print("TODO")
    return []

def gen_neg_skew_arr(size):
    print("TODO")
    return []

def gen_many_rep_arr(size):
    print("TODO")
    return []

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
    