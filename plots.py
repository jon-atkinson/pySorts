# pip is an idiot, can't access global packages so writes to local, of course
# then the program can exclusively access global so no dice. And the cherry on
# top is that there could be any number of pip/python distro/perms root causes
from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title('title')
root.iconbitmap()
root.geometry('400x200')

def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()


root.mainloop()