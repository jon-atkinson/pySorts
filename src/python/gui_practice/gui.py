# colour pallet
colour1 = "#B8D8D8"
colour2 = "#7A9E9F"
colour3 = "#4F6367"
colour4 = "#EEF5DB"
colour5 = "#FE5F55"

# from tkinter import *
# from tkinter import ttk

# root = Tk()

# def myClick():
#     myLabel = Label(root, text="Look! I clicked a button!!").grid(row=3,column=0)

# count = 2

# # Creating and gridding labels
# myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
# myLabel2 = Label(root, text="My Name is Jon Atkinson").grid(row=1, column=1)

# myButton = Button(root, text="Click Me!", state=DISABLED, fg="blue").grid(row=0,column=1)
# myButton = Button(root, text="No, Click Me!", padx=50, pady=5, command=myClick, fg="blue", bg="#000000").grid(row=1,column=0)

# # counter = Button(root, text=)

# root.mainloop()

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("pySorts")
root.geometry("720x480")
root.config(background=colour1)

guiStyle = ttk.Style()
guiStyle.configure("my.tButton", foreground="#334353")
guiStyle.configure("my.tFrame", background="#334353")

frame = ttk.Frame(root, style='My.TFrame')
frame.grid(column=1, row=1)

ttk.Button(frame, text='test', style='My.TButton').grid(column=0, row=0)
ttk.Button(frame, text='Test 2', style='My.TButton').grid(column=3, row=3)




# mainFrame = ttk.Frame(root, padding=10, bg="red")

# s.configure("frm.Tframe", background="red")
# tab1 = ttk.Frame(frm, style="frm.Tframe")
# frm.add(tab1, text="tab1")

# frm.grid()
# ttk.Label(frm, text="pySorts", font=("Arial", 25), foreground="red").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
