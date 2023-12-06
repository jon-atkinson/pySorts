from tkinter import *

root = Tk()

def myClick(count):
    myLabel = Label(root, text="Look! I clicked a button!!").grid(row=count,column=0)

count = 2

# Creating and gridding labels
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="My Name in Jon Atkinson").grid(row=1, column=1)

myButton = Button(root, text="Click Me!", state=DISABLED).grid(row=0,column=1)
myButton = Button(root, text="No, Click Me!", padx=50, pady=5, command=myClick(count)).grid(row=1,column=0)

# counter = Button(root, text=)

root.mainloop()