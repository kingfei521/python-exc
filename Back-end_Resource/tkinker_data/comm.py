from tkinter import ttk, messagebox

from register import App


class CheckButton(object):

    def foo(self, root):
        return ttk.Checkbutton(root, text='array', takefocus=0, variable=1)

singleton = CheckButton()


import threading

