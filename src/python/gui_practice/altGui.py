import tkinter as tk
from tkinter import ttk

class CustomGUI:
    # Color Pallet
    colour1 = "#B8D8D8"
    colour2 = "#7A9E9F"
    colour3 = "#4F6367"
    colour4 = "#EEF5DB"
    colour5 = "#FE5F55"

    def __init__(self, root):
        self.root = root
        self.root.title("pySorts")
        self.root.geometry("720x480")

        self.borderFrame = ttk.Frame(root, padding="10", style="Outer.TFrame")
        self.borderFrame.place(relx=0.5, rely=0.5, anchor="center")

        self.custom_style = ttk.Style()
        self.custom_style.configure("Outer.TFrame", background=self.colour1)
        self.custom_style.configure("CustomLabel.TLabel", background=self.colour4, padding=5)
        
        # border setup
        self.borderFrame= ttk.Frame(root, style="Outer.TFrame")
        self.borderFrame.grid(row=0, column=0, sticky="nsew")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # generate content
        label1 = ttk.Label(self.borderFrame, text="Label 1", style="CustomLabel.TLabel").grid(column=10, row=0)
        button1 = ttk.Button(self.borderFrame, text='test', style='My.TButton').grid(column=10, row=10)
        quitButton = ttk.Button(self.borderFrame, text='Quit', command=self.root.destroy, style='My.TButton').grid(column=100, row=100)
        # label2 = ttk.Label(self.borderFrame, text="Label 2", style="CustomLabel.TLabel")

        # label1.grid(row=0, column=0, padx=5, pady=5)
        # label2.grid(row=1, column=0, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomGUI(root)
    root.mainloop()