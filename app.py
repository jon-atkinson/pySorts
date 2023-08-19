import genDataSets
import sorts

def commandLoop():
    print(formatPrompt("input: "), end="")
    command = input()
    while(command != "q" and command != "Q"):
        match command:
            case "h":
                help_pySort()
            case "sel":
                print("n: ", end='')
                print(sorts.selectionSort(genDataSets.genRandArr(int(input()))))
            case "bub":
                print("n: ", end='')
                print(sorts.bubbleSort(genDataSets.genRandArr(int(input()))))
            case "ins":
                print("n: ", end='')
                print(sorts.insertionSort(genDataSets.genRandArr(int(input()))))
            case "hep":
                print("n: ", end='')
                print(sorts.heapSort(genDataSets.genRandArr(int(input()))))
            case "qck":
                print("n: ", end='')
                print(sorts.quickSort(genDataSets.genRandArr(int(input()))))
            case "mrg":
                print("n: ", end='')
                print(sorts.mergeSort(genDataSets.genRandArr(int(input()))))
            case "bck":
                print("n: ", end='')
                print(sorts.bucketSort(genDataSets.genRandArr(int(input()))))
            case "rdx":
                print("n: ", end='')
                print(sorts.radixSort(genDataSets.genRandArr(int(input()))))
            case "cnt":
                print("n: ", end='')
                print(sorts.countSort(genDataSets.genRandArr(int(input()))))
            case "shl":
                print("n: ", end='')
                print(sorts.shellSort(genDataSets.genRandArr(int(input()))))
            case "tim":
                print("n: ", end='')
                print(sorts.timSort(genDataSets.genRandArr(int(input()))))
            case "tre":
                print("n: ", end='')
                print(sorts.treeSort(genDataSets.genRandArr(int(input()))))
            case "cbe":
                print("n: ", end='')
                print(sorts.cubeSort(genDataSets.genRandArr(int(input()))))
            case _:
                print("command not recognised")
        print(formatPrompt("input: "), end="")
        command = input()

def help_pySort():
    print("\nAvailable commands include:")
    print("  - h: print this message")
    print("  - q or Q: quit the program")
    print("  - sel: selection sort")
    print("  - ins: selection sort")
    print("  - hep: selection sort")
    print("  - qck: selection sort")
    print("  - mrg: selection sort")
    print("  - bck: bucket sort")
    print("  - rdx: selection sort")
    print("  - cnt: selection sort")
    print("  - shl: selection sort")
    print("  - tim: selection sort")
    print("  - tre: selection sort")
    print("  - cbe: selection sort")

def formatPrompt(promptMsg):
    return ("\033[94m {}\033[00m".format(promptMsg)).strip()
    
if __name__ == '__main__': #
    print(formatPrompt("Welcome to pySort, please enter a command:"))
    commandLoop()
