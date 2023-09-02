import ctypes
import os

def compute_algo_comparisons(algo, in_strs, n, arr_type, num_reps, verbose):
    arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    c_arr = to_c_arr(arr, n)
    sortedArray = algo(c_arr, n)

    print("Initial: " + str(arr) + "\nFinal: ", end="")
    for i in range(n):
        print(sortedArray[i], "", end="")
 
def to_c_arr(arr, n):
    return (ctypes.c_int * n)(*arr)

def construct_c_algo(algo_ref):
    algo_ref.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    algo_ref.restype = ctypes.POINTER(ctypes.c_int)
    return algo_ref


script_dir = os.path.abspath(os.path.dirname(__file__))
lib_path = os.path.join(script_dir, "minRep.so")
minRep = ctypes.cdll.LoadLibrary(lib_path)
compute_algo_comparisons(construct_c_algo(minRep.heapSort), ["hepC"], 10, "rand", 1, True)
