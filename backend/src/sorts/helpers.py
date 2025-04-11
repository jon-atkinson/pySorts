import ctypes


def construct_c_algorithm(algo_ref):
    algo_ref.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    algo_ref.restype = ctypes.POINTER(ctypes.c_int)
    return algo_ref


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
