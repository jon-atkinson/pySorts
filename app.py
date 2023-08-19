import genDataSets

def commandLoop():
    print(formatPrompt("input: "), end="")
    command = input()
    while(command != "q" and command != "Q"):
        match command:
            case "h":
                help_pySort()
            case "sel":
                print(selectionSort(genDataSets.genRandArr(int(input()))))
            case _:
                print("command not recognised")
        print(formatPrompt("input: "), end="")
        command = input()

def help_pySort():
    print("\nAvailable commands include:")
    print("  - h: print this message")
    print("  - q or Q: quit the program")
    print("  - sel: selection sort")

def formatPrompt(promptMsg):
    return ("\033[94m {}\033[00m".format(promptMsg)).strip()
    
def selectionSort(arr):
    minIdx, currIdx = 0, 0
    for i in range(len(arr) - 1):
        for j in range(currIdx, len(arr)):
            if (arr[j] < arr[minIdx]):
                minIdx = j
        arr[minIdx], arr[currIdx] = arr[currIdx], arr[minIdx]
        minIdx, currIdx = currIdx + 1, currIdx + 1
    return arr
        
if __name__ == '__main__': #
    print(formatPrompt("Welcome to pySort, please enter a command:"))
    commandLoop()
