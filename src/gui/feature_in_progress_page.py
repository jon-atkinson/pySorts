import tkinter as tk
from tkinter import *
from tkinter import ttk

from colour import Colour


class FeatureInProgressPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=Colour.colour1)
        label = tk.Label(
            self,
            text="Feature Under Construction",
            font=("TKFixedFont", 40),
            bg=Colour.colour1,
            fg=Colour.colour2,
        )
        label.pack(pady=100, padx=100)
        button_container = ttk.Frame(self)
        button_container.pack()
        home_button = ttk.Button(
            button_container,
            text="Back to Home",
            style="Home.TButton",
            command=lambda: controller.show_frame("StartPage"),
        )
        home_button.grid(row=0, column=0, padx=100, pady=10)
        comp_algo_button = ttk.Button(
            button_container,
            text="Compare Algorithms",
            style="Home.TButton",
            command=lambda: controller.show_frame("CompareAlgorithmsPage"),
        )
        comp_algo_button.grid(row=0, column=1, padx=100, pady=10)
        comp_algo_button = ttk.Button(
            button_container,
            text="Compare Sortedness",
            style="Home.TButton",
            command=lambda: controller.show_frame("CompareSortednessPage"),
        )
        comp_algo_button.grid(row=0, column=2, padx=100, pady=10)
