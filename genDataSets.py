import random
import time

def genRandArr(size):
    array = []
    random.seed(time.time())
    for num in range(size):
        array.append(random.randint(0,size))
    return array

def genPosSkewArr(size):
    print("TODO")
    return []

def genNegSkewArr(size):
    print("TODO")
    return []

def genManyRepArr(size):
    print("TODO")
    return []

def genPreSortedArr(size):
    arr = []
    for i in range(size):
        arr.append(i)
    return arr

def genRevSortedArr(size):
    arr = []
    for i in range(size):
        arr.append(size - i)
    return arr
    