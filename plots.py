#%%
# pip is an idiot, can't access global packages so writes to local, of course
# then the program can exclusively access global so no dice. And the cherry on
# top is that there could be any number of pip/python distro/perms root causes

# from tkinter import *
# from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt


# root = Tk()
# root.title('title')
# root.iconbitmap()
# root.geometry('400x200')

# def graph():
#     house_prices = np.random.normal(200000, 25000, 5000)
#     plt.hist(house_prices, 50)
#     plt.show()


plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

x = np.array([5, 4, 1, 4, 5])
y = np.sort(x)

plt.title("Line graph")
plt.plot(x, y, color="red")

plt.show()
# %%
