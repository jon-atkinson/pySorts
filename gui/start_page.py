import tkinter as tk
from tkinter import *
from tkinter import ttk

from gui.colour import Colour


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=Colour.colour1)
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        compareAlgosButton = ttk.Button(
            self,
            text="Compare Algorithms",
            style="Home.TButton",
            command=lambda: controller.show_frame("CompareAlgorithmsPage"),
        )
        compareAlgosButton.grid(row=0, column=0, padx=10, pady=10)
        quitButton = ttk.Button(
            self, text="Quit", style="Home.TButton", command=parent.parent.destroy
        )
        quitButton.grid(row=0, column=1, padx=10, pady=10)
        compareSortednessButton = ttk.Button(
            self,
            text="Compare Algorithm Performance for Different Input Sortedness",
            style="Home.TButton",
            command=lambda: controller.show_frame("CompareSortednessPage"),
        )
        compareSortednessButton.grid(row=1, column=0, padx=10, pady=10)
        showGraphButton = ttk.Button(
            self,
            text="Most Recently Generated Graph",
            style="Home.TButton",
            command=lambda: controller.show_frame("GraphPage"),
        )
        showGraphButton.grid(row=1, column=1, padx=10, pady=10)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
