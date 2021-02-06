import tkinter
from collections import deque
from tkinter import *
from tkinter import ttk
master = Tk()
master.geometry('500x200')
text = """Fast Namasdasdasdasdasde\nJack LoveLi \nmingJse stan Sne. \n罗行
""".strip()
val = deque(maxlen=1)

def call(event1, filewin, p):
    a = event1.widget.cget('text')
    print(a[0:10])
    filewin.destroy()
    p.set(a[0:10])

def donothing(event, p):
    filewin = Toplevel(master)
    a = Label(filewin, text="Fast Name1 \n刘欢 \n迪丽热巴", wraplength=220, justify=tkinter.LEFT, bg='red')
    # a.bind('<Button-1>', lambda event1: call(event1,  filewin))
    a.grid(row=1, column=1, padx=10, pady=10)
    b = Label(filewin, text="Fast Name2 \n刘欢 \n迪丽热巴", wraplength=220, justify=tkinter.LEFT, bg='red')
    b.bind('<Button-1>', lambda event1: call(event1, filewin, p))
    b.grid(row=1, column=2, padx=10, pady=10)
    c = Label(filewin, text="Fast Name3 \n刘欢 \n迪丽热巴", wraplength=220, justify=tkinter.LEFT, bg='red')
    c.grid(row=1, column=3, padx=10, pady=10)
    c.grid_forget()
    d = Label(filewin, text="Fast Name4 \n刘欢 \n迪丽热巴", wraplength=220, justify=tkinter.LEFT, bg='red')
    d.grid(row=1, column=4, padx=10, pady=10)
    d.grid_forget()
    e = Label(filewin, text="Fast Name5 \n刘欢 \n迪丽热巴", wraplength=220, justify=tkinter.LEFT, bg='red')
    e.grid(row=2, column=1, padx=10, pady=10)
    f = Label(filewin, text="Fast Name6 \n刘欢 \n迪丽热巴", wraplength=220, justify=tkinter.LEFT, bg='red')

    f.grid(row=2, column=2, padx=10, pady=10)
    filewin.grab_set()



v = StringVar()
p = ttk.Entry(master, textvariable=v)

p.grid(row=0, column=0)


p.bind("<Button-1>", lambda event: donothing(event, v))

# master.grab_set()
# master.grab_release()
master.mainloop()