from tkinter import *
from tkinter import ttk

root_window = Tk()

img2 = PhotoImage("entryBorder", data="""
        R0lGODlhHQAdAOMNAAAAAAQGCAgLERkfLR0mODBFZTFFZTNIajtTezxTez1XgD5XgU
        Fch////////////ywAAAAAHQAdAAAEbHCQg5i9OGt0iFRaKGLKxBgCoK5s6woGc4Cp
        a9+AwFQM7ruYn1AVHP6KRhwyaVsyW87nKioFUKXXZ5a5TXaN32FYOD5eqsAzmlX2tZ
        XqNZGxYATkgAD9wCjUqgIFMgR1I4YZCx4TCYeGCR0DEQA7""")

oestyle = ttk.Style()
oestyle.element_create("blueborder", "image", "entryBorder",
                                   border=3, sticky="nsew")
oestyle.layout("OEntryStyle.TEntry",
               [('Entry.blueborder', {'children': [(
                   'Entry.padding', {'children': [(
                     'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})])
oestyle.configure("OEntryStyle.TEntry",
                 background="black",
                  foreground="gray")
oentry_v = StringVar()
oentry = ttk.Entry(root_window, style="OEntryStyle.TEntry", textvariable=oentry_v)
oentry.pack(padx=10, pady=10)
root_window.mainloop()