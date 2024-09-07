import readline
from typing import NewType
import python.operation as operation
import os
import traceback
import python.plot as plot

def commandLoop():
    command_str = input(formatPrompt("operation: "))
    command = command_str.split(" ")[0]
    command_args = command_str.split(" ")[1:]
    while(command != "q" and command != "Q"):
        try:
            match command:
                case "h":
                    helpPySort()
                case "algo":
                    operation.compare_sort_algos(command_args)
                case "sorting":
                    operation.compare_sortedness(command_args)
                case "plot":
                    plot.plot_algos_cli(command_args)
                case "clear":
                    os.system('clear')
                case _:
                    raise Exception("incorrect command format")
        except Exception as _:
            print(traceback.format_exc())
        command_str = input(formatPrompt("operation: "))
        command = command_str.split(" ")[0]
        command_args = command_str.split(" ")[1:]

def helpPySort():
    print("Available operations include:")
    print("  - algo: compares the runtime of different algorithms") 
    print("  - sorting: compares the runtime of different sortedness inputs of a given algorithm")
    print("  - plot: plots two algorithms' big O response for a given sortedness")

    print("\nAvailable modifiers (these can be combined): ")
    print(" -p pretty prints the output")
    print(" -o orders the output fastest to slowest (default ordering is user provided at input time)")

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
    print("  - bub: bubble sort")
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
    print("  - cbe: cube sort (unimplemented)")

def formatPrompt(promptMsg):
    return ("\033[94m {}\033[00m".format(promptMsg)).strip()

def runCLI():
    os.system('clear')
    print(formatPrompt("Welcome to pySorts, please enter a command:"))
    commandLoop()
