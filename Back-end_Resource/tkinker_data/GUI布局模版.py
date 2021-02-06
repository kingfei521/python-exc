from tkinter import *
import tkinter as tk
from tkinter import ttk


class ButtonManager(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.config(background = 'green')

        lblFrame = LabelFrame(self, controller)
        btnFrame = ButtonFrame(self, controller)

        lblFrame.pack(side="top", fill="x", expand=False)
        btnFrame.pack(side="top", fill="both", expand=True)

class LabelFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="blue")

        lblTitleBar = ttk.Label(self, text = 'TITLE BAR', background = 'grey', font = ("Arial", 20, "bold"))
        lblTextBar = ttk.Label(self, text = 'test text', background = 'grey', font = ("Arial", 16, "bold"))

        lblTitleBar.pack(side="top", fill="x")
        lblTextBar.pack(side="top", fill="x")

class ButtonFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="red")

        for row in range(7):
            self.grid_rowconfigure(row, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        b1 = tk.Button(self, text="Button 1")
        b2 = tk.Button(self, text="Button 2")
        b3 = tk.Button(self, text="Button 3")
        b4 = tk.Button(self, text="Button 4")
        b5 = tk.Button(self, text="Button 5")
        b6 = tk.Button(self, text="Button 6")
        b7 = tk.Button(self, text="Button 7")
        b8 = tk.Button(self, text="Button 8")
        b9 = tk.Button(self, text="Button 9")
        b10 = tk.Button(self, text="Button 10")

        b1.grid(row=0, column=0, sticky="nsew")
        b2.grid(row=0, column=1, sticky="nsew")
        b3.grid(row=1, column=0, sticky="nsew")
        b4.grid(row=1, column=1, sticky="nsew")
        b5.grid(row=2, column=0, sticky="nsew")
        b6.grid(row=2, column=1, sticky="nsew")
        b7.grid(row=3, column=0, columnspan=2, sticky="nsew")
        b8.grid(row=4, column=0, sticky="nsew")
        b9.grid(row=4, column=1, sticky="nsew")
        b10.grid(row=5, column=0, columnspan=2, sticky="nsew")

class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background="yellow")


class Interface(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self, background="bisque")
        # container.pack(fill="both", expand=True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        container.grid(row=0, column=0, sticky="nsew")

        bman = ButtonManager(container, controller=self)
        main = Main(container, controller=self)

        container.grid_columnconfigure(0, weight=1)
        container.grid_columnconfigure(1, weight=2)
        container.grid_rowconfigure(0, weight=1)

        bman.grid(row=0, column=0, sticky="nsew")
        main.grid(row=0, column=1, sticky="nsew")

interface = Interface()
interface.minsize(800, 480)
interface.mainloop()