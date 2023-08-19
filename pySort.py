import random
import time

def triangle():
    n = 10
    for row in range(n):
        print(('#'*(row+2)).ljust(n+1))

def fizzBuzz():
    for num in range(100):
        term = ""
        if (not (num % 3)):
            term += "Fizz"
        if (not (num % 5)):
            term += "Buzz"
        if (term == ""):
            term = str(num)
        print(term)

def commandLoop():
    print("input: ")
    command = input()
    while(command != "q" and command != "Q"):
        match command:
            case "h":
                help_pySort()
            case "sel":
                selectionSort()
            case _:
                print("command not recognised")
        print("input: ")
        command = input()

def help_pySort():
    print("\nAvailable commands include:")
    print("  - h: print this message")
    print("  - q or Q: quit the program")
    print("  - sel: selection sort")

def genRandArr(size):
    array = []
    random.seed(time.time())
    for num in range(size):
        array.append(random.randint(0,size))
    return array
    
def selectionSort():
    print("TODO: selection sort implementation")
    
if __name__ == '__main__': #
    welcomeMsg = "Welcome to pySort, please enter a command:"
    print(welcomeMsg)
    commandLoop()
