def selection_sort(arr):
    n = len(arr)
    min_idx = 0
    for curr_idx in range(n):
        for j in range(curr_idx, n):
            if (arr[j] < arr[min_idx]):
                min_idx = j
        arr[min_idx], arr[curr_idx] = arr[curr_idx], arr[min_idx]
        min_idx = curr_idx + 1
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swap_this = False
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_this = True
        if (swap_this == False):
            break
    return arr

def insertion_sort(arr):
    print("TODO - implement this sort")
    return arr

def heap_sort(arr):
    print("TODO - implement this sort")
    return arr

def quick_sort(arr):
    print("TODO - implement this sort")
    return arr

def merge_sort(arr):
    print("TODO - implement this sort")
    return arr

def bucket_sort(arr):
    print("TODO - implement this sort")
    return arr

def radix_sort(arr):
    print("TODO - implement this sort")
    return arr

def count_sort(arr):
    print("TODO - implement this sort")
    return arr

def shell_sort(arr):
    print("TODO - implement this sort")
    return arr

def tim_sort(arr):
    print("TODO - implement this sort")
    return arr

def tree_sort(arr):
    print("TODO - implement this sort")
    return arr

def cube_sort(arr):
    print("TODO - implement this sort")
    return arr
