from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

window = ThemedTk()


ttk.Label(window, text='Apples').grid(column=0, row=0)
ttk.Label(window, text='Oranges').grid(column=2, row=0)
ttk.Label(window, text='Pears').grid(column=4, row=0)
ttk.Label(window, text='Cherries').grid(column=0, row=2)
ttk.Label(window, text='Avocados').grid(column=2, row=2)
ttk.Label(window, text='Bananas').grid(column=4, row=2)
ttk.Separator(window, orient=HORIZONTAL).grid(row=1, columnspan=10, sticky=(W,E))
ttk.Separator(window, orient=VERTICAL).grid(row=0, column=3, rowspan=3, sticky=(S,N))

window.mainloop()