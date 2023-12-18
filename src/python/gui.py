from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from plot import plot_algos_gui
from statistics import median
import numpy as np
import math

# colour pallet
colour1 = "#B8D8D8"
colour2 = "#7A9E9F"
colour3 = "#4F6367"
colour4 = "#EEF5DB"
colour5 = "#FE5F55"

class app(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "pySorts algorithm runtime comparison tool")
        self.geometry("1280x720")

        container = tk.Frame(self)
        container.pack(expand=True, fill="both", side="top")
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}

        titleBar = tk.Frame(container, width=1280, height=100, borderwidth=20, background=colour3)
        title = tk.Label(titleBar, text="pySorts", font=("Quicksand", 16, "bold"), foreground=colour5, background=colour3)
        title.pack()
        title.configure(anchor="center")
        titleBar.pack(side="top", fill="both", expand=False)

        content = tk.Frame(container)
        content.parent = self
        content.pack(side="top", fill="both", expand=True)
        content.grid_rowconfigure(0, weight=1)
        content.grid_columnconfigure(0, weight=1)

        for F in (StartPage, CompareAlgorithmsPage, PageTwo, GraphPage):
            frame = F(content, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

        style = ttk.Style()
        style.configure(".",
                        font=("TkFixedFont", 10, "bold"),
                        background=colour1,
                        foreground=colour3)
        style.configure("TButton",
                        font=("TkFixedFont", 10, "bold", "underline"),
                        foreground=colour3,
                        background=colour4,
                        anchor="center")
        style.configure("Home.TButton",
                        padding=20)
        style.configure("Plot.Home.TButton",
                        background=colour5,
                        foreground=colour4)
        style.configure("Increment.TButton",
                        font=("TkFixedFont", 6, "bold"),
                        height=5,
                        width=5)
        style.configure("TCheckbutton",
                        background=colour1,
                        foreground=colour3,
                        indicatorcolor=colour4,
                        width=30,
                        anchor="w")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=colour1)
        self.controller = controller

        compareAlgosButton = ttk.Button(self, text="Compare Algorithms",
                                        style="Home.TButton",
                                        command=lambda: controller.show_frame(CompareAlgorithmsPage))
        compareAlgosButton.grid(row=0,
                                column=0,
                                padx=10,
                                pady=10)
        quitButton = ttk.Button(self, text="Quit",
                                style="Home.TButton",
                                command=parent.parent.destroy)
        quitButton.grid(row=0,
                        column=1,
                        padx=10,
                        pady=10)
        compareSortednessButton = ttk.Button(self, text="Compare Algorithm Performance for Different Input Sortedness",
                                             style="Home.TButton",
                                             command=lambda: controller.show_frame(PageTwo))
        compareSortednessButton.grid(row=1,
                                     column=0,
                                     padx=10,
                                     pady=10)
        showGraphButton = ttk.Button(self, text="Most Recently Generated Graph",
                                     style="Home.TButton",
                                     command=lambda: controller.show_frame(GraphPage))
        showGraphButton.grid(row=1,
                             column=1,
                             padx=10,
                             pady=10)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)


class CompareAlgorithmsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=colour1)
        self.columnconfigure(1, weight=1)
        self.controller = controller

        left_panel = ttk.Frame(self)
        left_panel.grid(row=0,
                        column=0)
        right_panel = ttk.Frame(self)
        right_panel.grid(row=0,
                        column=1,
                        sticky="ew")
        right_panel.columnconfigure(0, weight=1)

        algorithms = ["Bucket Sort    (py)",
                      "Bubble Sort    (py)",
                      "Count Sort     (py)",
                      "Cube Sort      (py) - TODO",
                      "Heap Sort      (py)",
                      "Insertion Sort (py)",
                      "Merge Sort     (py)",
                      "Quick Sort     (py)",
                      "Radix Sort     (py)",
                      "Selection Sort (py)",
                      "Shell Sort     (py)",
                      "Tim Sort       (py)",
                      "Tree Sort      (py)",
                      "Bucket Sort    (c) - TODO",
                      "Bubble Sort    (c)",
                      "Count Sort     (c) - TODO",
                      "Cube Sort      (c) - TODO",
                      "Heap Sort      (c)",
                      "Insertion Sort (c)",
                      "Merge Sort     (c) - TODO",
                      "Quick Sort     (c) - TODO",
                      "Radix Sort     (c) - TODO",
                      "Selection Sort (c)",
                      "Shell Sort     (c) - TODO",
                      "Tim Sort       (c) - TODO",
                      "Tree Sort      (c) - TODO"]
        self.selected_algos = []
        row_num = 0
        for algo in algorithms:
            var = tk.IntVar()
            checkbox = ttk.Checkbutton(left_panel,
                                   style="TCheckbutton",
                                   text=algo,
                                   variable=var)
            checkbox.grid(row=row_num,
                          column=0)
            row_num += 1
            self.selected_algos.append(var)

        button_frame = ttk.Frame(left_panel)
        button_frame.grid(row=row_num,
                          column=0,
                          sticky="w",
                          pady=10)
        select_all_algos_button = ttk.Button(button_frame, text="Select All",
                                             command=self.select_all_algos,
                                             width=10)
        select_all_algos_button.grid(row=0,
                                     column=0)
        deselect_all_algos_button = ttk.Button(button_frame, text="Deselect All",
                                             command=self.deselect_all_algos,
                                             width=10)
        deselect_all_algos_button.grid(row=0,
                                     column=1)
        select_py_algos_button = ttk.Button(button_frame, text="Select py",
                                             command=self.select_py_algos,
                                             width=10)
        select_py_algos_button.grid(row=1,
                                     column=0)
        select_c_algos_button = ttk.Button(button_frame, text="Select c",
                                             command=self.select_c_algos,
                                             width=10)
        select_c_algos_button.grid(row=1,
                                     column=1)
        max_row_num = row_num

        row_num = 0
        input_options = ["Sorted",
                         "Reverse Sorted",
                         "Random",
                         "Many Repeated",
                         "Positive Skew",
                         "Negative Skew"]
        self.selected_sortedness = tk.StringVar()
        for input_option in input_options:
            input_radio_button = ttk.Radiobutton(left_panel,
                                                 text=input_option,
                                                 variable=self.selected_sortedness,
                                                 value=input_option,
                                                 width=30)
                                                #  command=self.on_sortedness_selection)
            input_radio_button.grid(row=row_num,
                                    column=1,
                                    sticky="w")
            row_num += 1

        sliders_container = ttk.Frame(left_panel)
        sliders_container.grid(row=max_row_num,
                               column=1)

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
                             command=lambda: controller.show_frame(StartPage))
        home_button.grid(row=0,
                         column=0,
                         pady=10)

        plot_button = ttk.Button(right_panel,
                                 text="Plot",
                                 style="Plot.Home.TButton",
                                 command=lambda: self.show_graph())
        plot_button.grid(row=1,
                         column=0,
                         padx=20,
                         pady=20)
        
        lastGraphButton = ttk.Button(right_panel,
                                     text="Last Graph",
                                     style="Home.TButton",
                                     command=lambda: controller.show_frame(GraphPage))
        lastGraphButton.grid(row=2,
                     column=0,
                     pady=10)

        compare_sortedness_button = ttk.Button(right_panel,
                             text="Page Two",
                             style="Home.TButton",
                             command=lambda: controller.show_frame(PageTwo))
        compare_sortedness_button.grid(row=3,
                     column=0,
                     pady=10)

    def select_all_algos(self):
        for var in self.selected_algos:
            var.set(1)

    def deselect_all_algos(self):
        for var in self.selected_algos:
            var.set(0)

    def select_py_algos(self):
        for var in self.selected_algos[:13]:
            var.set(1)

    def select_c_algos(self):
        for var in self.selected_algos[13:]:
            var.set(1)

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

    def show_graph(self):
        alg_names = self.parse_algo_strs()
        start = self.min_sweep_val.get()
        stop = self.max_sweep_val.get()
        step = self.step_val.get()
        arr_type = self.parse_sortedness()
        num_reps = self.reps_val.get()
        n_steps, results = plot_algos_gui(alg_names, start, stop, step, arr_type, num_reps)
        self.controller.show_frame(GraphPage)
        graph = self.controller.frames[GraphPage]
        graph.originalResults = results
        graph.plot(results, n_steps, alg_names, num_reps)

    def parse_algo_strs(self):
        all_alg_names = ["bct",
                       "bub",
                       "cnt",
                       "cbe",
                       "hep",
                       "ins",
                       "mrg",
                       "qck",
                       "rdx",
                       "sel",
                       "shl",
                       "tim",
                       "tre",
                       "bctC",
                       "bubC",
                       "cntC",
                       "cbeC",
                       "hepC",
                       "insC",
                       "mrgC",
                       "qckC",
                       "rdxC",
                       "selC",
                       "shlC",
                       "timC",
                       "treC"]
        alg_names = []
        for count, num in enumerate(self.selected_algos):
            if num.get() == 1:
                alg_names.append(all_alg_names[count])
        return alg_names
    
    def parse_sortedness(self):
        match self.selected_sortedness.get():
            case "Sorted":
                return "sorted"
            case "Reverse Sorted":
                return "reverse"
            case "Random":
                return "rand"
            case "Many Repeated":
                return "manyRep"
            case "Positive Skew":
                return "posSkew"
            case "Negative Skew":
                return "negSkew"
            case _:
                raise Exception("no match found for sortedness")

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=colour1)
        label = tk.Label(self, text="Page Two!!!")
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(CompareAlgorithmsPage))
        button2.pack()


class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=colour1)
        self.results = {}
        self.originalResults = {}
        self.n_steps = 0
        self.alg_names = []
        self.num_reps = 0

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.leftPanel = ttk.Frame(self)
        self.leftPanel.grid(row=0,
                            column=0,
                            sticky="nsew",
                            padx=(5,5),
                            pady=5)
        self.rightPanel = ttk.Frame(self)
        self.rightPanel.grid(row=0,
                             column=1,
                             padx=(0, 5))

        homeButton = ttk.Button(self.rightPanel,
                                text="Back to Home",
                                style="Home.TButton",
                                command=lambda: controller.show_frame(StartPage))
        homeButton.grid(row=0,
                        column=0,
                        padx=10,
                        pady=(10, 0),
                        sticky="nsew")

        compareAlgosButton = ttk.Button(self.rightPanel,
                                        text="Back to Cmp Alg",
                                        style="Home.TButton",
                                        command=lambda: controller.show_frame(CompareAlgorithmsPage))
        compareAlgosButton.grid(row=1,
                                column=0,
                                padx=10,
                                pady=(10, 0),
                                sticky="nsew")

        resetFiltersButton = ttk.Button(self.rightPanel,
                                        text="Reset Filters",
                                        style="Home.TButton",
                                        command=self.resetFilters)
        resetFiltersButton.grid(row=2,
                                column=0,
                                padx=10,
                                pady=(10, 0),
                                sticky="nsew")

        removePeaksButton = ttk.Button(self.rightPanel,
                                      text="Remove Peaks\n(median filter)",
                                      command=self.medianFilterPlots)
        removePeaksButton.grid(row=3,
                              column=0,
                              padx=10,
                              pady=(10, 0),
                              sticky="nsew")

        slideContain = ttk.Frame(self.rightPanel)
        slideContain.grid(row=4,
                          column=0,
                          padx=10)
        self.medianFilterSize = tk.IntVar(value=3)
        self.medianFilterSizeSlider = ttk.Scale(slideContain,
                                               from_=3,
                                               to=25,
                                               orient="horizontal",
                                               length=100,
                                               command=self.onMedianKernelSizeSliderChange,
                                               variable=self.medianFilterSize)
        self.medianFilterSizeSlider.grid(row=0,
                                        column=0)
        self.medianFilterSizeLabel = ttk.Label(slideContain,
                                          text="M Size: 03")
        self.medianFilterSizeLabel.grid(row=0,
                                       column=1)

        smoothPlotsButton = ttk.Button(self.rightPanel,
                                      text="Smooth Plots\n(conv. filter)",
                                      command=self.convolveFilterPlots)
        smoothPlotsButton.grid(row=5,
                               column=0,
                               padx=10,
                               pady=(10, 0),
                               sticky="nsew")

        slideContain = ttk.Frame(self.rightPanel)
        slideContain.grid(row=6,
                          column=0,
                          padx=10)
        self.gaussKernelSize = tk.IntVar(value=3)
        self.gaussKernelSizeSlider = ttk.Scale(slideContain,
                                               from_=3,
                                               to=25,
                                               orient="horizontal",
                                               length=100,
                                               command=self.onGaussKernelSizeSliderChange,
                                               variable=self.gaussKernelSize)
        self.gaussKernelSizeSlider.grid(row=0,
                                        column=0)
        self.gaussKernelSizeLabel = ttk.Label(slideContain,
                                              text="K Size: 03")
        self.gaussKernelSizeLabel.grid(row=0,
                                       column=1)

        self.leftPanel.f = Figure(dpi=100)
        self.leftPanel.f.set_size_inches(11, 6.4, forward=False)
        self.canvas = FigureCanvasTkAgg(self.leftPanel.f, self.leftPanel)
        self.canvas.draw()
    
    def onGaussKernelSizeSliderChange(self, value):
        intVal = max(1, round(float(self.gaussKernelSize.get())))
        oddVal = intVal + (intVal % 2 == 0)
        self.gaussKernelSize.set(oddVal)
        self.gaussKernelSizeLabel.config(text=f"K Size: {round(float(self.gaussKernelSize.get())):02}")

    def onMedianKernelSizeSliderChange(self, value):
        intVal = max(1, round(float(self.medianFilterSize.get())))
        oddVal = intVal + (intVal % 2 == 0)
        self.medianFilterSize.set(oddVal)
        self.medianFilterSizeLabel.config(text=f"M Size: {round(float(self.medianFilterSize.get())):02}")

    def plot(self, results, n_steps, alg_names, num_reps):
        self.leftPanel.f.clear()
        self.results = results
        self.n_steps = n_steps
        self.alg_names = alg_names
        self.num_reps = num_reps

        width = self.leftPanel.winfo_width() / 100
        height = self.leftPanel.winfo_height() / 100
        self.leftPanel.f.set_size_inches(width, height, forward=False)

        graph = self.leftPanel.f.add_subplot(111)
        self.canvas.get_tk_widget().grid(row=0,column=0,sticky="nsew")
        
        for elem in results:
            graph.plot(n_steps, results[elem])

        graph.legend(alg_names)
        graph.set_title(f"Average runtimes for {num_reps} repetition(s) of each algorithm")
        graph.set_xlabel("Array Length (n)")
        graph.set_ylabel("Time Cost (s)")
        self.canvas.draw()

    def resetFilters(self):
        self.plot(self.originalResults, self.n_steps, self.alg_names, self.num_reps)

    def medianFilterPlots(self):
        halfLen = self.medianFilterSize.get() // 2
        smoothedResults = {}
        for algo in self.results:
            smoothed = []
            paddedResults = self.results[algo][:halfLen][::-1] + self.results[algo] + self.results[algo][-halfLen:][::-1]
            for r in range(halfLen, len(paddedResults) - halfLen):
                smoothed.append(median(paddedResults[r-halfLen:r+halfLen+1]))
            smoothedResults[algo] = smoothed
        self.plot(smoothedResults, self.n_steps, self.alg_names, self.num_reps)

    def convolveFilterPlots(self):
        kernel = self.genKernel()
        smoothedResults = {}
        buffLen = self.gaussKernelSize.get() // 2

        for algo in self.results:
            smoothedResults[algo] = self.results[algo][:buffLen] + list(np.convolve(self.results[algo], kernel, mode="valid")) + self.results[algo][-buffLen:]

        self.plot(smoothedResults, self.n_steps, self.alg_names, self.num_reps)

    def genKernel(self):
        length = self.gaussKernelSize.get()
        sigma = 1
        r = range(-int(length/2),int(length/2)+1)
        return [1 / (sigma * math.sqrt(2*math.pi)) * math.exp(-float(x)**2/(2*sigma**2)) for x in r]


app = app()
app.mainloop()