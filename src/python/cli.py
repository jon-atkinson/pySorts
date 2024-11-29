import requests
import os
import traceback
import python.plot as plot
from config import API_URL as API_URL

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
                    # operation.compare_sort_algos(command_args)
                    compare_algorithms(command_args)
                # case "sorting":
                    # operation.compare_sortedness(command_args)
                    # compare_sortedness(command_args)
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

def compare_algorithms(command_args):
    """
    Sends a POST request ot he compare_algorithms API route and priunts the results to terminal.
    """
    try:
        algorithms = command_args[0].split(",")
        low = int(command_args[1])
        high = int(command_args[2])
        arr_type = command_args[3]
        num_reps = int(command_args[4])
        step = int(command_args[5])

        request_body = {
            "algorithms": [
                {
                    "algorithm": algorithm.strip(),
                    "language": "python"
                } for algorithm in algorithms
            ],
            "low": low,
            "high": high,
            "arr_type": arr_type,
            "num_reps": num_reps,
            "step": step,
        }

        response = requests.post(API_URL, json=request_body)

        if response.status_code == 200:
            results = response.json()["results"]
            print("Results:")
            for algorithm, language, series in results:
                print(f"Algorithm: {algorithm}, Language: {language}")
                for length, avg_time in series:
                    print(f"  Length: {length}, Average Time: {avg_time}")
        else:
            print(f"Error: {response.status_code} - {response.text}") 

    except Exception as e:
        print(f"Error processing command: {str(e)}")

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

if __name__ == "__main__":
    runCLI()