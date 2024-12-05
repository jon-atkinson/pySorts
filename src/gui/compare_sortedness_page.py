import tkinter as tk
from tkinter import *
from tkinter import ttk
from gui.plot import plot_sortedness_gui
from gui.colour import Colour
import gui.gui_config as gui_config

class CompareSortednessPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=Colour.colour1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.controller = controller

        left_panel = ttk.Frame(self)
        left_panel.grid(row=0,
                        column=0,
                        sticky="esw")
        right_panel = ttk.Frame(self)
        right_panel.grid(row=0,
                        column=1,
                        sticky="esw")
        right_panel.columnconfigure(0, weight=1)

        self.algorithms = {}
        for language, algorithms in gui_config.config["algorithms"].items():
            for algorithm in algorithms:
                key = f"{algorithm.title()} ({language})"
                self.algorithms[key] = {
                    "algorithm": algorithm,
                    "language": language
                }
        self.selected_algorithm = tk.StringVar()
        row_num = 0
        for idx, key in enumerate(self.algorithms.keys()):
            input_radio_button = ttk.Radiobutton(left_panel,
                                                 text=key,
                                                 variable=self.selected_algorithm,
                                                 value=key,
                                                 width=30)
            input_radio_button.grid(row=idx,
                                    column=0,
                                    sticky="w")
            row_num += 1
        self.selected_algorithm.set("Bubble Sort    (c)");







        self.sortedness_options = {
            "Sorted": "sorted",
            "Reverse Sorted": "reverse sorted",
            "Random": "random",
            # "Many Repeats": "many repeats",
            "Positive Skew": "positive skew",
            "Negative Skew": "negative skew"
        }
        self.selected_sortedness = {}
        row_num = 0
        for sortedness in self.sortedness_options.keys():
            var = tk.IntVar()
            checkbox = ttk.Checkbutton(left_panel,
                                   style="TCheckbutton",
                                   text=sortedness,
                                   variable=var)
            checkbox.grid(row=row_num,
                          column=1,
                          sticky="w")
            row_num += 1
            self.selected_sortedness.update({sortedness:var})






        button_frame = ttk.Frame(left_panel)
        button_frame.grid(row=len(self.algorithms),
                          column=0,
                          sticky="w",
                          pady=10)

        select_all_sortedness_button = ttk.Button(button_frame, text="Select All",
                                             command=self.select_all_sortedness,
                                             width=10)
        select_all_sortedness_button.grid(row=0,
                                     column=0)
        deselect_all_sortedness_button = ttk.Button(button_frame, text="Deselect All",
                                             command=self.deselect_all_sortedness,
                                             width=10)
        deselect_all_sortedness_button.grid(row=0,
                                     column=1)

        sliders_container = ttk.Frame(left_panel)
        sliders_container.grid(row=len(self.algorithms),
                               column=1,
                               sticky="s")

        self.sweep_start = ttk.Label(sliders_container,
                                     text="Start: 00001")
        self.sweep_start.grid(row=0,
                         column=0,
                         sticky="w")
        self.min_sweep_val = tk.IntVar(value=1)
        self.min_slider = ttk.Scale(sliders_container,
                               from_=1,
                               to=10000,
                               orient="horizontal",
                               length=500,
                               command=self.on_min_slider_change,
                               variable=self.min_sweep_val)
        self.min_slider.grid(row=0,
                         column=1,
                         pady=2)
        self.min_sweep_subt_hundred_button = ttk.Button(sliders_container,
                                              text="-100",
                                              style="Increment.TButton",
                                              command=self.min_sweep_subt_hundred)
        self.min_sweep_subt_hundred_button.grid(row=0,
                                      column=2,
                                      pady=2)
        self.min_sweep_subt_ten_button = ttk.Button(sliders_container,
                                              text="-10",
                                              style="Increment.TButton",
                                              command=self.min_sweep_subt_ten)
        self.min_sweep_subt_ten_button.grid(row=0,
                                      column=3,
                                      pady=2)
        self.min_sweep_add_ten_button = ttk.Button(sliders_container,
                                              text="+10",
                                              style="Increment.TButton",
                                              command=self.min_sweep_add_ten)
        self.min_sweep_add_ten_button.grid(row=0,
                                      column=4,
                                      pady=2)
        self.min_sweep_add_hundred_button = ttk.Button(sliders_container,
                                              text="+100",
                                              style="Increment.TButton",
                                              command=self.min_sweep_add_hundred)
        self.min_sweep_add_hundred_button.grid(row=0,
                                      column=5,
                                      pady=2)

        self.sweep_end = ttk.Label(sliders_container,
                                     text="Stop: 00001")
        self.sweep_end.grid(row=1,
                         column=0,
                         sticky="w")
        self.max_sweep_val = tk.IntVar(value=1)
        self.max_slider = ttk.Scale(sliders_container,
                               from_=1,
                               to=10000,
                               orient="horizontal",
                               length=500,
                               command=self.on_max_slider_change,
                               variable=self.max_sweep_val)
        self.max_slider.grid(row=1,
                         column=1,
                         pady=2)
        self.max_sweep_subt_hundred_button = ttk.Button(sliders_container,
                                              text="-100",
                                              style="Increment.TButton",
                                              command=self.max_sweep_subt_hundred)
        self.max_sweep_subt_hundred_button.grid(row=1,
                                      column=2,
                                      pady=2)
        self.max_sweep_subt_ten_button = ttk.Button(sliders_container,
                                              text="-10",
                                              style="Increment.TButton",
                                              command=self.max_sweep_subt_ten)
        self.max_sweep_subt_ten_button.grid(row=1,
                                      column=3,
                                      pady=2)
        self.max_sweep_add_ten_button = ttk.Button(sliders_container,
                                              text="+10",
                                              style="Increment.TButton",
                                              command=self.max_sweep_add_ten)
        self.max_sweep_add_ten_button.grid(row=1,
                                      column=4,
                                      pady=2)
        self.max_sweep_add_hundred_button = ttk.Button(sliders_container,
                                              text="+100",
                                              style="Increment.TButton",
                                              command=self.max_sweep_add_hundred)
        self.max_sweep_add_hundred_button.grid(row=1,
                                      column=5,
                                      pady=2)

        self.step = ttk.Label(sliders_container,
                                     text="Step: 0001")
        self.step.grid(row=2,
                         column=0,
                         sticky="w")
        self.step_val = tk.IntVar(value=1)
        self.step_slider = ttk.Scale(sliders_container,
                               from_=1,
                               to=1000,
                               orient="horizontal",
                               length=500,
                               command=self.on_step_slider_change,
                               variable=self.step_val)
        self.step_slider.grid(row=2,
                         column=1,
                         pady=2)
        self.step_subt_hundred_button = ttk.Button(sliders_container,
                                              text="-100",
                                              style="Increment.TButton",
                                              command=self.step_subt_hundred)
        self.step_subt_hundred_button.grid(row=2,
                                      column=2,
                                      pady=2)
        self.step_subt_ten_button = ttk.Button(sliders_container,
                                              text="-10",
                                              style="Increment.TButton",
                                              command=self.step_subt_ten)
        self.step_subt_ten_button.grid(row=2,
                                      column=3,
                                      pady=2)
        self.step_add_ten_button = ttk.Button(sliders_container,
                                              text="+10",
                                              style="Increment.TButton",
                                              command=self.step_add_ten)
        self.step_add_ten_button.grid(row=2,
                                      column=4,
                                      pady=2)
        self.step_add_hundred_button = ttk.Button(sliders_container,
                                              text="+100",
                                              style="Increment.TButton",
                                              command=self.step_add_hundred)
        self.step_add_hundred_button.grid(row=2,
                                      column=5,
                                      pady=2)

        self.repeats = ttk.Label(sliders_container,
                                     text="Reps: 0001")
        self.repeats.grid(row=3,
                         column=0,
                         sticky="w")
        self.reps_val = tk.IntVar(value=1)
        self.reps_slider = ttk.Scale(sliders_container,
                               from_=1,
                               to=1000,
                               orient="horizontal",
                               length=500,
                               command=self.on_repeats_slider_change,
                               variable=self.reps_val)
        self.reps_slider.grid(row=3,
                         column=1,
                         pady=2)
        self.reps_subt_hundred_button = ttk.Button(sliders_container,
                                              text="-100",
                                              style="Increment.TButton",
                                              command=self.reps_subt_hundred)
        self.reps_subt_hundred_button.grid(row=3,
                                      column=2,
                                      pady=2)
        self.reps_subt_ten_button = ttk.Button(sliders_container,
                                              text="-10",
                                              style="Increment.TButton",
                                              command=self.reps_subt_ten)
        self.reps_subt_ten_button.grid(row=3,
                                      column=3,
                                      pady=2)
        self.reps_add_ten_button = ttk.Button(sliders_container,
                                              text="+10",
                                              style="Increment.TButton",
                                              command=self.reps_add_ten)
        self.reps_add_ten_button.grid(row=3,
                                      column=4,
                                      pady=2)
        self.reps_add_hundred_button = ttk.Button(sliders_container,
                                              text="+100",
                                              style="Increment.TButton",
                                              command=self.reps_add_hundred)
        self.reps_add_hundred_button.grid(row=3,
                                      column=5,
                                      pady=2)






        home_button = ttk.Button(right_panel,
                             text="Home",
                             style="Home.TButton",
                             command=lambda: controller.show_frame("StartPage"))
        home_button.grid(row=0,
                         column=0,
                         pady=10)

        self.plot_button_text = tk.StringVar(value="Plot")
        self.plot_button = ttk.Button(right_panel,
                                 textvariable=self.plot_button_text,
                                 style="Plot.Home.TButton",
                                 command=lambda: self.click_plot_btn())
        self.plot_button.grid(row=1,
                         column=0,
                         padx=20,
                         pady=20)
        
        lastGraphButton = ttk.Button(right_panel,
                                     text="Last Graph",
                                     style="Home.TButton",
                                     command=lambda: controller.show_frame("GraphPage"))
        lastGraphButton.grid(row=2,
                     column=0,
                     pady=10)

        compare_sortedness_button = ttk.Button(right_panel,
                             text="Feature Under Construction",
                             style="Home.TButton",
                             command=lambda: controller.show_frame("FeatureInProgressPage"))
        compare_sortedness_button.grid(row=3,
                     column=0,
                     pady=10)

    def select_all_sortedness(self):
        for sortedness in self.sortedness_options.keys():
            self.selected_sortedness[sortedness].set(1)

    def deselect_all_sortedness(self):
        for sortedness in self.sortedness_options.keys():
            self.selected_sortedness[sortedness].set(0)

    def select_py_algos(self):
        for algo in self.algorithms.keys():
            if algo[-3:-1] == "py": self.selected_algos[algo].set(1)

    def select_c_algos(self):
        for algo in self.algorithms.keys():
            if algo[-2] == "c": self.selected_algos[algo].set(1)

    def on_min_slider_change(self, value):
        self.sweep_start.config(text=f"Start: {round(float(value)):05}")

    def min_sweep_subt_hundred(self):
        val = max(self.min_slider.cget("from"), self.min_sweep_val.get() - 100)
        self.min_sweep_val.set(val)
        self.on_min_slider_change(val)

    def min_sweep_subt_ten(self):
        val = max(self.min_slider.cget("from"), self.min_sweep_val.get() - 10)
        self.min_sweep_val.set(val)
        self.on_min_slider_change(val)
    
    def min_sweep_add_ten(self):
        val = min(self.min_slider.cget("to"), self.min_sweep_val.get() + 10)
        self.min_sweep_val.set(val)
        self.on_min_slider_change(val)
    
    def min_sweep_add_hundred(self):
        val = min(self.min_slider.cget("to"), self.min_sweep_val.get() + 100)
        self.min_sweep_val.set(val)
        self.on_min_slider_change(val)
    
    def on_max_slider_change(self, value):
        self.sweep_end.config(text=f"Stop: {round(float(value)):05}")

    def max_sweep_subt_hundred(self):
        val = max(self.max_slider.cget("from"), self.max_sweep_val.get() - 100)
        self.max_sweep_val.set(val)
        self.on_max_slider_change(val)

    def max_sweep_subt_ten(self):
        val = max(self.max_slider.cget("from"), self.max_sweep_val.get() - 10)
        self.max_sweep_val.set(val)
        self.on_max_slider_change(val)
    
    def max_sweep_add_ten(self):
        val = min(self.max_slider.cget("to"), self.max_sweep_val.get() + 10)
        self.max_sweep_val.set(val)
        self.on_max_slider_change(val)
    
    def max_sweep_add_hundred(self):
        val = min(self.max_slider.cget("to"), self.max_sweep_val.get() + 100)
        self.max_sweep_val.set(val)
        self.on_max_slider_change(val)

    def step_subt_hundred(self):
        val = max(self.step_slider.cget("from"), self.step_val.get() - 100)
        self.step_val.set(val)
        self.on_step_slider_change(val)

    def step_subt_ten(self):
        val = max(self.step_slider.cget("from"), self.step_val.get() - 10)
        self.step_val.set(val)
        self.on_step_slider_change(val)
    
    def step_add_ten(self):
        val = min(self.step_slider.cget("to"), self.step_val.get() + 10)
        self.step_val.set(val)
        self.on_step_slider_change(val)
    
    def step_add_hundred(self):
        val = min(self.step_slider.cget("to"), self.step_val.get() + 100)
        self.step_val.set(val)
        self.on_step_slider_change(val)

    def reps_subt_hundred(self):
        val = max(self.step_slider.cget("from"), self.reps_val.get() - 100)
        self.reps_val.set(val)
        self.on_repeats_slider_change(val)

    def reps_subt_ten(self):
        val = max(self.reps_slider.cget("from"), self.reps_val.get() - 10)
        self.reps_val.set(val)
        self.on_repeats_slider_change(val)
    
    def reps_add_ten(self):
        val = min(self.reps_slider.cget("to"), self.reps_val.get() + 10)
        self.reps_val.set(val)
        self.on_repeats_slider_change(val)
    
    def reps_add_hundred(self):
        val = min(self.reps_slider.cget("to"), self.reps_val.get() + 100)
        self.reps_val.set(val)
        self.on_repeats_slider_change(val)

    def on_step_slider_change(self, value):
        self.step.config(text=f"Step: {round(float(value)):04}")

    def on_repeats_slider_change(self, value):
        self.repeats.config(text=f"Reps: {round(float(value)):04}")

    def click_plot_btn(self):
        try:
            self.plot_button_text.set("Sorting...")
            self.plot_button.state(["!pressed", "!active"])
            self.plot_button.state(["disabled"])
            self.plot_button.update_idletasks()
            self.show_graph()   
        finally:
            self.plot_button.state(["!disabled"])
            self.plot_button_text.set("Plot")

    def show_graph(self):
        alg_name = self.algorithms[self.selected_algorithm.get()]
        start = self.min_sweep_val.get()
        stop = self.max_sweep_val.get()
        step = self.step_val.get()
        arr_types = self.parse_arr_types()
        num_reps = self.reps_val.get()

        n_steps, results = plot_sortedness_gui(alg_name, start, stop, step, arr_types, num_reps)
        graph = self.controller.frames["GraphPage"]
        graph.originalResults = results
        graph.plot(
            results,
            n_steps,
            arr_types,
            num_reps,
            f"Average runtimes for {num_reps} repetition{'' if num_reps <= 1 else num_reps} of each sortedness with {alg_name}"
        )
        self.controller.show_frame("GraphPage")

    def parse_arr_types(self):
        result = []
        for sortedness in self.sortedness_options.keys():
            if self.selected_sortedness[sortedness].get() == 1:
                result.append(self.sortedness_options[sortedness])
        return result

    # def parse_algo_strs(self):
    #     alg_names = []
    #     for algo in self.selected_algos:
    #         if self.selected_algos[algo].get() == 1:
    #             alg_names.append(self.algorithms[algo])
    #     return alg_names
    
    # def parse_sortedness(self):
    #     match self.selected_sortedness.get():
    #         case "Sorted":
    #             return "sorted"
    #         case "Reverse Sorted":
    #             return "reverse"
    #         case "Random":
    #             return "rand"
    #         case "Many Repeated":
    #             return "manyRep"
    #         case "Positive Skew":
    #             return "posSkew"
    #         case "Negative Skew":
    #             return "negSkew"
    #         case _:
                # raise Exception("no match found for sortedness")