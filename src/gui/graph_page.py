import math
import tkinter as tk
from statistics import median
from tkinter import *
from tkinter import ttk

import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from gui.colour import Colour


class GraphPage(tk.Frame):

    def __init__(self, parent, controller):
        matplotlib.use("TkAgg")
        tk.Frame.__init__(self, parent, background=Colour.colour1)
        self.results = {}
        self.originalResults = {}
        self.n_steps = 0
        self.alg_names = []
        self.num_reps = 0

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.leftPanel = ttk.Frame(self)
        self.leftPanel.grid(row=0, column=0, sticky="nsew", padx=(5, 5), pady=5)
        self.rightPanel = ttk.Frame(self)
        self.rightPanel.grid(row=0, column=1, padx=(0, 5))

        homeButton = ttk.Button(
            self.rightPanel,
            text="Back to Home",
            style="Home.TButton",
            command=lambda: controller.show_frame("StartPage"),
        )
        homeButton.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        compareAlgosButton = ttk.Button(
            self.rightPanel,
            text="Back to Cmp Alg",
            style="Home.TButton",
            command=lambda: controller.show_frame("CompareAlgorithmsPage"),
        )
        compareAlgosButton.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nsew")

        compareAlgosButton = ttk.Button(
            self.rightPanel,
            text="Back to Cmp Srt",
            style="Home.TButton",
            command=lambda: controller.show_frame("CompareSortednessPage"),
        )
        compareAlgosButton.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="nsew")

        resetFiltersButton = ttk.Button(
            self.rightPanel,
            text="Reset Filters",
            style="Home.TButton",
            command=self.resetFilters,
        )
        resetFiltersButton.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="nsew")

        removePeaksButton = ttk.Button(
            self.rightPanel,
            text="Remove Peaks\n(median filter)",
            command=self.medianFilterPlots,
        )
        removePeaksButton.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="nsew")

        slideContain = ttk.Frame(self.rightPanel)
        slideContain.grid(row=5, column=0, padx=10)
        self.medianFilterSize = tk.IntVar(value=3)
        self.medianFilterSizeSlider = ttk.Scale(
            slideContain,
            from_=3,
            to=25,
            orient="horizontal",
            length=100,
            command=self.onMedianKernelSizeSliderChange,
            variable=self.medianFilterSize,
        )
        self.medianFilterSizeSlider.grid(row=0, column=0)
        self.medianFilterSizeLabel = ttk.Label(slideContain, text="M Size: 03")
        self.medianFilterSizeLabel.grid(row=0, column=1)

        smoothPlotsButton = ttk.Button(
            self.rightPanel,
            text="Smooth Plots\n(conv. filter)",
            command=self.convolveFilterPlots,
        )
        smoothPlotsButton.grid(row=6, column=0, padx=10, pady=(10, 0), sticky="nsew")

        slideContain = ttk.Frame(self.rightPanel)
        slideContain.grid(row=7, column=0, padx=10)
        self.gaussKernelSize = tk.IntVar(value=3)
        self.gaussKernelSizeSlider = ttk.Scale(
            slideContain,
            from_=3,
            to=25,
            orient="horizontal",
            length=100,
            command=self.onGaussKernelSizeSliderChange,
            variable=self.gaussKernelSize,
        )
        self.gaussKernelSizeSlider.grid(row=0, column=0)
        self.gaussKernelSizeLabel = ttk.Label(slideContain, text="K Size: 03")
        self.gaussKernelSizeLabel.grid(row=0, column=1)

        self.leftPanel.f = Figure(dpi=100)
        self.leftPanel.f.set_size_inches(11, 6.4, forward=False)
        self.canvas = FigureCanvasTkAgg(self.leftPanel.f, self.leftPanel)
        self.canvas.draw()

    def onGaussKernelSizeSliderChange(self, value):
        intVal = max(1, round(float(self.gaussKernelSize.get())))
        oddVal = intVal + (intVal % 2 == 0)
        self.gaussKernelSize.set(oddVal)
        self.gaussKernelSizeLabel.config(
            text=f"K Size: {round(float(self.gaussKernelSize.get())):02}"
        )

    def onMedianKernelSizeSliderChange(self, value):
        intVal = max(1, round(float(self.medianFilterSize.get())))
        oddVal = intVal + (intVal % 2 == 0)
        self.medianFilterSize.set(oddVal)
        self.medianFilterSizeLabel.config(
            text=f"M Size: {round(float(self.medianFilterSize.get())):02}"
        )

    def plot(self, results, n_steps, alg_names, num_reps, title):
        self.leftPanel.f.clear()
        self.results = results
        self.n_steps = n_steps
        self.alg_names = alg_names
        self.num_reps = num_reps
        self.last_title = title

        width = self.leftPanel.winfo_width() / 100
        height = self.leftPanel.winfo_height() / 100
        self.leftPanel.f.set_size_inches(width, height, forward=False)

        graph = self.leftPanel.f.add_subplot(111)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky="nsew")

        for elem in results:
            graph.plot(n_steps, results[elem])

        graph.legend(alg_names)
        graph.set_title(title)
        graph.set_xlabel("Array Length (n)")
        graph.set_ylabel("Time Cost (s)")
        self.canvas.draw()

    def resetFilters(self):
        self.plot(
            self.originalResults,
            self.n_steps,
            self.alg_names,
            self.num_reps,
            self.last_title,
        )

    def medianFilterPlots(self):
        halfLen = self.medianFilterSize.get() // 2
        smoothedResults = {}
        for algo in self.results:
            smoothed = []
            paddedResults = (
                self.results[algo][:halfLen][::-1]
                + self.results[algo]
                + self.results[algo][-halfLen:][::-1]
            )
            for r in range(halfLen, len(paddedResults) - halfLen):
                smoothed.append(median(paddedResults[r - halfLen : r + halfLen + 1]))
            smoothedResults[algo] = smoothed
        self.plot(
            smoothedResults,
            self.n_steps,
            self.alg_names,
            self.num_reps,
            self.last_title,
        )

    def convolveFilterPlots(self):
        kernel = self.genKernel()
        smoothedResults = {}
        buffLen = self.gaussKernelSize.get() // 2

        for algo in self.results:
            smoothedResults[algo] = (
                self.results[algo][:buffLen]
                + list(np.convolve(self.results[algo], kernel, mode="valid"))
                + self.results[algo][-buffLen:]
            )

        self.plot(
            smoothedResults,
            self.n_steps,
            self.alg_names,
            self.num_reps,
            self.last_title,
        )

    def genKernel(self):
        length = self.gaussKernelSize.get()
        sigma = 1
        r = range(-int(length / 2), int(length / 2) + 1)
        return [
            1
            / (sigma * math.sqrt(2 * math.pi))
            * math.exp(-float(x) ** 2 / (2 * sigma**2))
            for x in r
        ]
