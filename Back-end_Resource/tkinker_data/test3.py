import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import time

root =ThemedTk()
root.geometry('400x400')
label = ttk.Label(root, text="Text on the screen", font=('Times New Roman',  '80'), )
label.place(x= 10, y=10)

# time.sleep(1000)

label.destroy()

root.mainloop()