import random
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import font

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

        for F in (StartPage, CompareAlgorithmsPage, PageTwo, PageThree):
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
        style.configure("TCheckbutton",
                        background=colour1,
                        foreground=colour3,
                        indicatorcolor=colour4,
                        width=30,
                        anchor="w")
        style.configure("Diagnosis.TFrame",
                        background="magenta")

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=colour1)
        self.controller = controller

        button = ttk.Button(self, text="Compare Algorithms",
                            style="Home.TButton",
                            command=lambda: controller.show_frame(CompareAlgorithmsPage))
        button.grid(row=0,column=0)
        button4 = ttk.Button(self, text="Quit",
                            style="Home.TButton",
                            command=parent.parent.destroy)
        button4.grid(row=0, column=1)
        button2 = ttk.Button(self, text="Compare Algorithm Performance for Different Input Sortedness",
                            style="Home.TButton",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=1,column=0)
        button3 = ttk.Button(self, text="Most Recently Generated Graph",
                            style="Home.TButton",
                            command=self.show_graph)
        button3.grid(row=1, column=1)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

    def show_graph(self):
        self.controller.show_frame(PageThree)
        graph = self.controller.frames[PageThree]
        graph.plot()

class CompareAlgorithmsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=colour1)
        self.columnconfigure(1, weight=1)

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
                      "Cube Sort      (py)",
                      "Heap Sort      (py)",
                      "Insertion Sort (py)",
                      "Merge Sort     (py)",
                      "Quick Sort     (py)",
                      "Radix Sort     (py)",
                      "Selection Sort (py)",
                      "Shell Sort     (py)",
                      "Tim Sort       (py)",
                      "Tree Sort      (py)",
                      "Bucket Sort    (c)",
                      "Bubble Sort    (c)",
                      "Count Sort     (c)",
                      "Cube Sort      (c)",
                      "Heap Sort      (c)",
                      "Insertion Sort (c)",
                      "Merge Sort     (c)",
                      "Quick Sort     (c)",
                      "Radix Sort     (c)",
                      "Selection Sort (c)",
                      "Shell Sort     (c)",
                      "Tim Sort       (c)",
                      "Tree Sort      (c)"]
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
                                             command=self.select_all_algos)
        select_all_algos_button.grid(row=0,
                                     column=0)
        deselect_all_algos_button = ttk.Button(button_frame, text="Deselect All",
                                             command=self.deselect_all_algos)
        deselect_all_algos_button.grid(row=0,
                                     column=1)
        select_py_algos_button = ttk.Button(button_frame, text="Select py",
                                             command=self.select_py_algos)
        select_py_algos_button.grid(row=1,
                                     column=0)
        select_c_algos_button = ttk.Button(button_frame, text="Select c",
                                             command=self.select_c_algos)
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
                                                 command=self.on_sortedness_selection)
            input_radio_button.grid(row=row_num,
                                    column=1,
                                    sticky="w")
            row_num += 1
        
        sliders_container = ttk.Frame(left_panel)
        sliders_container.grid(row=max_row_num,
                               column=1)
        self.sweep_start = ttk.Label(sliders_container,
                                     text="Start: 00000")
        self.sweep_start.grid(row=0,
                         column=0)
        min_sweep_val = tk.IntVar()
        min_slider = ttk.Scale(sliders_container,
                               from_=1,
                               to=10000,
                               orient="horizontal",
                               length=500,
                               command=self.on_min_slider_change,
                               variable=min_sweep_val)
        min_slider.grid(row=0,
                         column=1,
                         pady=10)

        self.sweep_end = ttk.Label(sliders_container,
                                     text="Stop: 00000")
        self.sweep_end.grid(row=1,
                         column=0)
        max_sweep_val = tk.IntVar()
        max_slider = ttk.Scale(sliders_container,
                               from_=1,
                               to=10000,
                               orient="horizontal",
                               length=500,
                               command=self.on_max_slider_change,
                               variable=max_sweep_val)
        max_slider.grid(row=1,
                         column=1,
                         pady=10)

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
                                 command=lambda: print("TODO: implement this button's functionality"))
        plot_button.grid(row=1,
                         column=0,
                         padx=20,
                         pady=20)
        compare_sortedness_button = ttk.Button(right_panel,
                             text="Page Two",
                             style="Home.TButton",
                             command=lambda: controller.show_frame(PageTwo))
        compare_sortedness_button.grid(row=2,
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

    def on_sortedness_selection(self):
        print(self.selected_sortedness.get())

    def on_min_slider_change(self, value):
        self.sweep_start.config(text=f"Start: {round(float(value)):05}")

    def on_max_slider_change(self, value):
        self.sweep_end.config(text=f"Stop: {round(float(value)):05}")

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


class PageThree(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=colour1)
        label = tk.Label(self, text="Graph Page!")
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        self.f = Figure(figsize=(5,5), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.f, self)

    def plot(self):
        self.f.clear()
        a = self.f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8,9,10],[random.randint(1,34) for _ in range(10)])
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

app = app()
app.mainloop()