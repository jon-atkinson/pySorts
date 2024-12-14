import ctypes
import os

import src.arrays as arrays_manager
import src.sorts.helpers as helpers
import src.sorts.python.python_sorts as sort_impls

API_URL = "http://127.0.0.1:8000"
"""
pySorts backend API address
"""

# load the c sorting algorithm implementations and expose in path
script_dir = os.path.abspath(os.path.dirname(__file__))
lib_path = os.path.join(script_dir, "sorts/c/cSorts.so")
cSorts = ctypes.cdll.LoadLibrary(lib_path)

"""
Dict of languages, each of which is a dict with keys-value maps for all sorting
algorithms implemented in that language
"""
algorithms = {
    "python": {
        "bucket sort": sort_impls.bucket_sort,
        "bubble sort": sort_impls.bubble_sort,
        "count sort": sort_impls.count_sort,
        "heap sort": sort_impls.heap_sort,
        "insertion sort": sort_impls.insertion_sort,
        "merge sort": sort_impls.merge_sort,
        "quick sort": sort_impls.quick_sort,
        "radix sort": sort_impls.radix_sort,
        "selection sort": sort_impls.selection_sort,
        "shell sort": sort_impls.shell_sort,
        "tim sort": sort_impls.tim_sort,
        "tree sort": sort_impls.tree_sort,
    },
    "c": {
        # "bucket sort": sort_impls.construct_c_algorithm(cSorts.bucketSort),
        "bubble sort": helpers.construct_c_algorithm(cSorts.bubbleSort),
        # "count sort": sort_impls.construct_c_algorithm(cSorts.countSort),
        "heap sort": helpers.construct_c_algorithm(cSorts.heapSort),
        "insertion sort": helpers.construct_c_algorithm(cSorts.insertionSort),
        # "merge sort": sort_impls.construct_c_algorithm(cSorts.mergeSort),
        # "quick sort": sort_impls.construct_c_algorithm(cSorts.quickSort),
        # "radix sort": sort_impls.construct_c_algorithm(cSorts.radixSort),
        "selection sort": helpers.construct_c_algorithm(cSorts.selectionSort),
        # "shell sort": sort_impls.construct_c_algorithm(cSorts.shellSort),
        # "tim sort": sort_impls.construct_c_algorithm(cSorts.timSort),
        # "tree sort": sort_impls.construct_c_algorithm(cSorts.treeSort),
    },
}

arrays = {
    "random": lambda n: arrays_manager.generate_random_array(n),
    "normal": lambda n: arrays_manager.generate_normal_array(n),
    "sorted": lambda n: arrays_manager.generate_sorted_array(n),
    "reverse sorted": lambda n: arrays_manager.generate_reverse_sorted_array(n),
    "positive skew": lambda n: arrays_manager.generate_positive_skew_array(n),
    "negative skew": lambda n: arrays_manager.generate_negative_skew_array(n),
    "many repeats": lambda n: arrays_manager.generate_many_repeats_array(n),
}
