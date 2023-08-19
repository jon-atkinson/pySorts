def selectionSort(arr):
    minIdx, currIdx = 0, 0
    for i in range(len(arr) - 1):
        for j in range(currIdx, len(arr)):
            if (arr[j] < arr[minIdx]):
                minIdx = j
        arr[minIdx], arr[currIdx] = arr[currIdx], arr[minIdx]
        minIdx, currIdx = currIdx + 1, currIdx + 1
    return arr

def bubbleSort(arr):
    print("TODO - implement this sort")
    return arr

def insertionSort(arr):
    print("TODO - implement this sort")
    return arr

def heapSort(arr):
    print("TODO - implement this sort")
    return arr

def quickSort(arr):
    print("TODO - implement this sort")
    return arr

def mergeSort(arr):
    print("TODO - implement this sort")
    return arr

def bucketSort(arr):
    print("TODO - implement this sort")
    return arr

def radixSort(arr):
    print("TODO - implement this sort")
    return arr

def countSort(arr):
    print("TODO - implement this sort")
    return arr

def shellSort(arr):
    print("TODO - implement this sort")
    return arr

def timSort(arr):
    print("TODO - implement this sort")
    return arr

def treeSort(arr):
    print("TODO - implement this sort")
    return arr

def cubeSort(arr):
    print("TODO - implement this sort")
    return arr
