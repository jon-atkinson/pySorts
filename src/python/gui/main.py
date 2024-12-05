import tkinter as tk
from tkinter import *
from tkinter import ttk
from python.gui.colour import Colour
from python.gui.compare_algorithms_page import CompareAlgorithmsPage
from python.gui.feature_in_progress_page import FeatureInProgressPage
from python.gui.graph_page import GraphPage
from python.gui.start_page import StartPage
from python.gui.compare_sortedness_page import CompareSortednessPage
import requests
import python.gui.gui_config as gui_config


class app(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "pySorts sorting algorithm runtime comparison tool")
        self.geometry("1280x720")

        gui_config.config = self.fetch_config()

        container = tk.Frame(self)
        container.pack(expand=True, fill="both", side="top")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        titleBar = tk.Frame(container, width=1280, height=100, borderwidth=20, background=Colour.colour3)
        title = tk.Label(titleBar, text="pySorts", font=("Quicksand", 30, "bold"), foreground=Colour.colour5, background=Colour.colour3)
        title.pack()
        title.configure(anchor="center")
        titleBar.pack(side="top", fill="both", expand=False)

        content = tk.Frame(container)
        content.parent = self
        content.pack(side="top", fill="both", expand=True)
        content.grid_rowconfigure(0, weight=1)
        content.grid_columnconfigure(0, weight=1)

        self.frames = {
            "StartPage": StartPage,
            "CompareAlgorithmsPage": CompareAlgorithmsPage,
            "FeatureInProgressPage": FeatureInProgressPage,
            "GraphPage": GraphPage,
            "CompareSortednessPage": CompareSortednessPage
        }
        for key in self.frames.keys():
            frame = self.frames[key](content, self)
            self.frames[key] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame("StartPage")

        style = ttk.Style()
        style.configure(".",
                        font=("TkFixedFont", 10, "bold"),
                        background=Colour.colour1,
                        foreground=Colour.colour3)
        style.configure("TButton",
                        font=("TkFixedFont", 10, "bold", "underline"),
                        foreground=Colour.colour3,
                        background=Colour.colour4,
                        anchor="center")
        style.configure("Home.TButton",
                        padding=20)
        style.configure("Plot.Home.TButton",
                        background=Colour.colour5,
                        foreground=Colour.colour4)
        style.configure("Increment.TButton",
                        font=("TkFixedFont", 6, "bold"),
                        height=5,
                        width=5)
        style.configure("TCheckbutton",
                        background=Colour.colour1,
                        foreground=Colour.colour3,
                        indicatorcolor=Colour.colour4,
                        width=30,
                        anchor="w")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def fetch_config(self):
        """
        Makes a GET request to fetch backend data and stores it in the shared state.

        Returns:
            dict: The data fetched from the backend.
        """
        try:
            response = requests.get(gui_config.API_URL + "/config")
            response.raise_for_status()
            data = response.json()
            return data
        except requests.RequestException as e:
            print(f"Error fetching backend data: {str(e)}")
            return {}

app = app()
app.mainloop()

def main():
    return