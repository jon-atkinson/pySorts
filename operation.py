import sorts
import genDataSets
import timeit

def timeSortAlgo():
    print("Enter Algorithm: ", end = "")
    inStr = input().strip()
    algo = getAlgo(inStr)
    print("Enter n: ", end = "")
    n = int(input())
    print("Enter input sortedness: ", end = "")
    arr = getArr(input().strip(), n)
    if (algo == None or arr == None):
        print("Error: algo or arr didn't populate correctly")
        return None
    print(inStr + "\t\t" + str(timeit.timeit(lambda: algo(arr), number=1)))
    
def raceSortAlgos():
    return
    
def getAlgo(matchStr):
    match matchStr:
        case "sel":
            return sorts.selectionSort
        case "ins":
            return sorts.insertionSort
        case "hep":
            return sorts.heapSort
        case "qck":
            return sorts.quickSort
        case "mrg":
            return sorts.mergeSort
        case "bct":
            return sorts.bucketSort
        case "rdx":
            return sorts.radixSort
        case "cnt":
            return sorts.countSort
        case "shl":
            return sorts.shellSort
        case "tim":
            return sorts.timSort
        case "tre":
            return sorts.treeSort
        case "cbe":
            return sorts.cubeSort
        case _:
            return None
    
def getArr(inStr, n):
    match inStr:
        case "sorted":
            return genDataSets.genPreSortedArr(n)
        case "reverse":
            return genDataSets.genRevSortedArr(n)
        case "rand":
            return genDataSets.genRandArr(n)
        case "manyRep":
            return genDataSets.genManyRepArr(n)
        case "posSkew":
            return genDataSets.genPosSkewArr(n)
        case "negSkew":
            return genDataSets.genNegSkewArr(n)
        case _:
            return None
