import tkinter
from tkinter import ttk
from ttkthemes import ThemedTk
class MakeGUI(object):
    def __init__(self,root):
        self.root = root
        self.root.title(u"Title")
        ## build frame
        self.mainframe = ttk.Frame(self.root, padding=(6, 6, 12, 12))
        self.mainframe.grid(sticky='nwse')
        for column in range(3):
            self.mainframe.columnconfigure(column, weight=1)
        self.mainframe.rowconfigure(1, weight=1)

        ## text labels
        ttk.Label(self.mainframe, text=u"Label Title", anchor='center',
                font=("Helvetica", 32)).grid(in_=self.mainframe,
                        column=0, row=0, columnspan=3, sticky="ew")

        self.lfdata = ttk.Labelframe(self.mainframe, padding=(6, 6, 12, 12),
                text='Labelframe')
        self.lfdata.grid(column=0, columnspan=3, row=1, sticky='nsew')
        info = (u"Source Filename", u"Source Text", u"Converted Text",
                u"Cleaned Source", u"Cleaned Converted", u"Details")
        for i, item in enumerate(info):
            ttk.Label(self.lfdata, text=u"%s:" % item).grid(in_=self.lfdata,
                    column=0, row=i, sticky='w')

        ## buttons
        btn = (u"Close", u"Next", u"Prev")
        for i, item in enumerate(btn):
            ttk.Button(self.mainframe, text=item).grid(in_=self.mainframe,
                    column=i, row=3)

def main():
    root = ThemedTk()
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    makeGUI = MakeGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()