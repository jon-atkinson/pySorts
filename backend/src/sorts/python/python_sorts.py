from sorts.python.avl import avl_insert, avl_to_sorted_array


def selection_sort(arr, n):
    min_idx = 0

    for curr_idx in range(n):
        for j in range(curr_idx, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[min_idx], arr[curr_idx] = arr[curr_idx], arr[min_idx]
        min_idx = curr_idx + 1

    return arr


def bubble_sort(arr, n):
    for i in range(n):
        swap = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        if swap == False:
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


def heap_sort(arr, n):
    build_max_heap(arr, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        j, index = 0, 0
        while True:
            index = 2 * j + 1
            if index < (i - 1) and arr[index] < arr[index + 1]:
                index += 1
            if index < i and arr[j] < arr[index]:
                arr[j], arr[index] = arr[index], arr[j]
            j = index
            if index >= i:
                break

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


def quick_sort(arr, n):
    stack = [(0, n - 1)]
    while stack:
        low, high = stack.pop()
        if low < high:
            pivot_index = partition_with_median_of_three(arr, low, high)
            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))
    return arr


def partition_with_median_of_three(arr, low, high):
    pivot_index = median_of_three(arr, low, high)
    pivot = arr[pivot_index]

    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def median_of_three(arr, low, high):
    mid = (low + high) // 2
    a, b, c = arr[low], arr[mid], arr[high]

    if (a <= b <= c) or (c <= b <= a):
        return mid
    elif (b <= a <= c) or (c <= a <= b):
        return low
    else:
        return high


def merge_sort(arr, n):
    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left, mid)
        merge_sort(right, n - mid)
        i = j = k = 0
        while i < mid and j < n - mid:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < mid:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < n - mid:
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def bucket_sort(arr, n):
    if n <= 1:
        return arr
    if n >= 10:
        num_buckets = 10
    else:
        num_buckets = 2

    rnge = n / num_buckets
    buckets = []

    for i in range(num_buckets):
        buckets.append([])

    for i in range(n):
        delta = arr[i] / rnge - int(arr[i] / rnge)
        if delta == 0 and arr[i] != 0:
            buckets[int(arr[i] / rnge) - 1].append(arr[i])
        else:
            buckets[int(arr[i] / rnge)].append(arr[i])

    for i in range(num_buckets):
        bucket_len = len(buckets[i])
        if bucket_len > 1:
            buckets[i] = quick_sort(buckets[i], bucket_len)

    idx = 0
    for bucket in buckets:
        for i in bucket:
            arr[idx] = i
            idx += 1

    return arr


def radix_sort(arr, n):
    exp = 1
    while n / exp >= 1:
        radix_count_help(arr, n, exp)
        exp *= 10
    return arr


def radix_count_help(arr, n, exp):
    out = [0] * n
    count = [0] * 10

    for i in range(n):
        idx = arr[i] // exp
        count[idx % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        idx = arr[i] // exp
        out[count[idx % 10] - 1] = arr[i]
        count[idx % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = out[i]


def count_sort(arr, n):
    count = [0] * (n + 1)

    for i in range(n):
        count[arr[i]] += 1

    idx = 0
    for i in range(n + 1):
        num = count[i]
        while num > 0:
            arr[idx] = i
            idx += 1
            num -= 1

    return arr


def shell_sort(arr, n):
    interval = n // 2
    while interval > 0:
        i = interval
        while i < n:
            j = i - interval
            while j >= 0:
                if arr[j + interval] > arr[j]:
                    break
                else:
                    arr[j + interval], arr[j] = arr[j], arr[j + interval]
                j = j - interval
            i += 1
        interval = interval // 2
    return arr


def tim_sort(arr, n):
    run_size = calc_run_size(n)

    for first in range(0, n, run_size):
        last = min(first + run_size - 1, n - 1)
        arr[first : last + 1] = insertion_sort(arr[first : last + 1], last - first + 1)

    merge_size = run_size
    while merge_size < n:
        for left in range(0, n, 2 * merge_size):
            mid = min(n - 1, left + merge_size - 1)
            right = min((left + 2 * merge_size - 1), n - 1)
            if mid < right:
                tim_merge(arr, left, mid, right)

        merge_size *= 2
    return arr


def calc_run_size(n):
    minRun = 32
    run = 0
    while n >= minRun:
        run |= n & 1
        n >>= 1
    return n + run


def tim_merge(arr, left_idx, mid_idx, right_idx):
    n1, n2 = mid_idx - left_idx + 1, right_idx - mid_idx
    (
        left,
        right,
    ) = (
        [],
        [],
    )

    for i in range(0, n1):
        left.append(arr[left_idx + i])
    for i in range(0, n2):
        right.append(arr[mid_idx + i + 1])

    i, j, k = 0, 0, left_idx
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


def tree_sort(arr, n):
    tree = None
    for num in arr:
        tree = avl_insert(tree, num)
    avl_to_sorted_array(tree, arr)

    return arr


def cube_sort(arr, n):
    print("TODO - implement this sort")
    return arr
