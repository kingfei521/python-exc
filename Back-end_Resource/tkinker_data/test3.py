# importing tkinter 
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askyesno

# creating root 
root = Tk()
root.geometry('200x100')

input_text = StringVar()

# This class is used to add styling 
# to any widget which are available 
style = ttk.Style()
style.configure('TEntry', foreground='green')

entry1 = ttk.Entry(root, textvariable=input_text, justify=CENTER,
                   font=('courier', 15, 'bold'))
entry1.focus_force()
entry1.pack(side=TOP, ipadx=30, ipady=10)

save = ttk.Button(root, text='Save', command=lambda: askyesno(
    'Confirm', 'Do you want to save?'))
save.pack(side=TOP, pady=10)

root.mainloop() 