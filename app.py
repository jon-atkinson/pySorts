import genDataSets
import sorts
import operation

def commandLoop():
    print(formatPrompt("operation: "), end="")
    command = input()
    while(command != "q" and command != "Q"):
        match command:
            case "h":
                helpPySort()
            case "time":
                operation.timeSortAlgo()
            case "race":
                operation.raceSortAlgos()
            # eventually have each of the following non-default calls be handled by a handler that
            # takes n the sort function (https://www.geeksforgeeks.org/passing-function-as-an-argument-in-python/),
            # sorted-ness of the input array and returns the

            # ideal eventual control flow:
            #              ask user for operation (time, race, etc.?)
            #                  /                            \
            #       time = ask for algo, n,         race = ask for algos as a space seperated string of strings
            #       input sortedness                         |
            #                  \                       ask for algo names (3 letter codes)
            #                   \                            |
            #                    \                   ask for input sortedness
            #                     \                         /
            # generate printout for all run algos format: algoName\t\t<time_taken in ms (timeit)>
            # (consider sorting this output for fastest runtime to slowest)
            case _:
                print("operation not recognised")
        print(formatPrompt("operation: "), end="")
        command = input()

def helpPySort():
    print("\nAvailable operations include:")
    print("  - time: times one algorithm")
    print("  - race: compares runtimes of two algorithms")

    print("\nAvailable input array configurations include:")
    print("  - sorted: pre-sorted array of n ints")
    print("  - reverse: reverse-sorted array of n ints")
    print("  - rand: randomly generated array of n ints")
    print("  - manyRep: array of n ints which is randomly distributed but has many repeated values")
    print("  - posSkew: randomly generated array of n ints with more smaller numbers")
    print("  - negSkew: randomly generated array of n ints with more larger numbers")

    print("\nAvailable sorting algorithms include:")
    print("  - h: print this message")
    print("  - q or Q: quit the program")
    print("  - sel: selection sort")
    print("  - ins: insertion sort")
    print("  - hep: heap sort")
    print("  - qck: quick sort")
    print("  - mrg: merge sort")
    print("  - bct: bucket sort")
    print("  - rdx: radix sort")
    print("  - cnt: count sort")
    print("  - shl: shell sort")
    print("  - tim: tim sort")
    print("  - tre: tree sort")
    print("  - cbe: cube sort")

def formatPrompt(promptMsg):
    return ("\033[94m {}\033[00m".format(promptMsg)).strip()
    
if __name__ == '__main__': #
    print(formatPrompt("Welcome to pySort, please enter a command:"))
    commandLoop()
