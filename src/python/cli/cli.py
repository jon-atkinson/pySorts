import os

import requests

from python.cli.cli_config import API_URL as API_URL
import python.cli.compare_algorithms as compare_algorithms
import python.cli.compare_sortedness as compare_sortedness


def command_loop(configuration: dict):
    """
    Main command loop for the cli frontend

    Args:
        configuration (dict): Backend API configuration

    Raises:
        ValueError: invalid command or filename input
    """
    command = input(formatPrompt("operation: ")).split(" ")
    while command[0] not in ["q", "Q", "quit", "Quit"]:
        try:
            match command[0]:
                case "h":
                    helpPySort()
                case "algo":
                    if len(command) > 2:
                        raise (
                            ValueError(
                                f"algo expected single filename argument, received={command[1:]}"
                            )
                        )
                    compare_algorithms.compare_algorithms(command[1], configuration)
                case "sorting":
                    compare_sortedness.compare_sortedness(command[1], configuration)
                case "clear":
                    os.system("clear")
                case _:
                    raise ValueError(
                        f'incorrect command format. Expected one of "h", "algo", "sorting", Recieved={command}'
                    )
        except ValueError as e:
            print(e)
        command = input(formatPrompt("operation: ")).split(" ")

def helpPySort():
    print("Usage: algo query_filename")

def formatPrompt(promptMsg):
    return ("\033[94m {}\033[00m".format(promptMsg)).strip()

def runCLI():
    os.system("clear")
    print(formatPrompt("Welcome to pySorts, please enter a command:"))

    try:
        response = requests.get(API_URL + "/config")
        if response.status_code == 200:
            command_loop(response.json())
        else:
            print(
                f"Error fetching sorter configuration: {response.status_code} - {response.text}"
            )

    except Exception as e:
        print(f"Generic Error Caught: {str(e)}")


if __name__ == "__main__":
    runCLI()
