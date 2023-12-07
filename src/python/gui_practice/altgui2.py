import random
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# colour pallet
colour1 = "#B8D8D8"
colour2 = "#7A9E9F"
colour3 = "#4F6367"
colour4 = "#EEF5DB"
colour5 = "#FE5F55"

class app(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "pySorts runtime comparison tool")
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
        content.pack(side="top", fill="both", expand=True)
        content.grid_rowconfigure(0, weight=1)
        content.grid_columnconfigure(0, weight=1)

        # setting up app pages
        for F in (StartPage, CompareAlgorithmsPage, PageTwo, PageThree):
            frame = F(content, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=colour1)
        self.controller = controller
        button = ttk.Button(self, text="Compare Algorithms",
                            command=lambda: controller.show_frame(CompareAlgorithmsPage))
        button.grid(row=1,column=0)
        button2 = ttk.Button(self, text="Compare Algorithm Performance for Different Input Sortedness",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=1,column=1)
        button3 = ttk.Button(self, text="Graph Page",
                            command=self.show_graph)
        button3.grid(row=1,column=3)

    def show_graph(self):
        self.controller.show_frame(PageThree)
        graph = self.controller.frames[PageThree]
        graph.plot()

class CompareAlgorithmsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, background=colour1)
        label = tk.Label(self, text="Page One!!!")
        label.pack(pady=10,padx=10)
        label2 = tk.Label(self, text="colour1", foreground=colour1)
        label2.pack(pady=10,padx=10)
        label3 = tk.Label(self, text="colour2", foreground=colour2)
        label3.pack(pady=10,padx=10)
        label4 = tk.Label(self, text="colour3", foreground=colour3)
        label4.pack(pady=10,padx=10)
        label5 = tk.Label(self, text="colour4", foreground=colour4)
        label5.pack(pady=10,padx=10)
        label6 = tk.Label(self, text="colour5", foreground=colour5)
        label6.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
        button2 = ttk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


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