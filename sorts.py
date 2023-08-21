def selection_sort(arr, n):
    min_idx = 0
    for curr_idx in range(n):
        for j in range(curr_idx, n):
            if (arr[j] < arr[min_idx]):
                min_idx = j
        arr[min_idx], arr[curr_idx] = arr[curr_idx], arr[min_idx]
        min_idx = curr_idx + 1
    return arr

def bubble_sort(arr, n):
    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if (swap == False):
            break
    return arr

def insertion_sort(arr, n):
    for i in range(1, n):
        val = arr[i]
        j = i - 1
        while j >= 0 and val < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val
    return arr

def build_max_heap(arr, n):
    for i in range(n):
        if arr[i] > arr[parent_idx(i)]:
            j = i
            while arr[j] > arr[parent_idx(j)]:
                (arr[j], arr[parent_idx(j)]) = (arr[parent_idx(j)], arr[j])
                j = parent_idx(j)
 
def parent_idx(idx):
    return int((idx - 1) / 2)

def heap_sort(arr, n):
    build_max_heap(arr, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        j, index = 0, 0
        while True:
            index = 2 * j + 1
            if (index < (i - 1) and arr[index] < arr[index + 1]):
                index += 1
            if index < i and arr[j] < arr[index]:
                arr[j], arr[index] = arr[index], arr[j]
            j = index
            if index >= i:
                break
    return arr

def quick_sort(arr, n):
    return quicksort_help(arr, 0, n)

def quicksort_help(arr, low, high):
    if low < high:
        piv = partition(arr, low, high)
        quicksort_help(arr, low, piv)
        quicksort_help(arr, piv + 1, high)
    return arr

def median_of_three(arr, low, high):
    mid = (low + high - 1) // 2
    a = arr[low]
    b = arr[mid]
    c = arr[high - 1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, high - 1
    if b <= c <= a:
        return c, high - 1
    return a, low

def partition(arr, low, high):
    pivot, pidx = median_of_three(arr, low, high)
    arr[low], arr[pidx] = arr[pidx], arr[low]
    i = low + 1
    for j in range(low + 1, high, 1):
        if (arr[j] < pivot):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def merge_sort(arr, n):
    print("TODO - implement this sort")
    return arr

def bucket_sort(arr, n):
    print("TODO - implement this sort")
    return arr

def radix_sort(arr, n):
    print("TODO - implement this sort")
    return arr

def count_sort(arr, n):
    print("TODO - implement this sort")
    return arr

def shell_sort(arr, n):
    print("TODO - implement this sort")
    return arr

def tim_sort(arr, n):
    print("TODO - implement this sort")
    return arr

def tree_sort(arr, n):
    print("TODO - implement this sort")
    return arr

def cube_sort(arr, n):
    print("TODO - implement this sort")
    return arr

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if (arr[i] > arr[i + 1]):
            return False
    return True

if __name__ == "__main__":
    import gen_data_sets as gen_data_sets
    n = 3970
    algorithm = quick_sort
    option = 0
    if option == 0:
        print("\n", is_sorted(algorithm(gen_data_sets.gen_rand_arr(n), n)))
        print("\n", is_sorted(algorithm(gen_data_sets.gen_pre_sorted_arr(n), n)))
        print("\n", is_sorted(algorithm(gen_data_sets.gen_rev_sorted_arr(n), n)))
        print("\n", is_sorted(algorithm(gen_data_sets.gen_many_rep_arr(n), n)))
    else:
        print("\n", algorithm(gen_data_sets.gen_rand_arr(n), n))
        print("\n", algorithm(gen_data_sets.gen_pre_sorted_arr(n), n))
        print("\n", algorithm(gen_data_sets.gen_rev_sorted_arr(n), n))
        print("\n", algorithm(gen_data_sets.gen_many_rep_arr(n), n))