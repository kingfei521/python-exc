from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.font as tkfont
pixmap_themes = [
   "arc",
   "blue",
   "clearlooks",
   "elegance",
   "kroc",
   "plastik",
   "radiance",
   "winxpblue"
]


class App(object):
    def __init__(self, root):
        self.root = root
        self.root.title("测试数据生成器")
        self.root.geometry('1250x700+0+0')
        self.root.resizable(0, 0)
        # self.button_list = []
        self.root.set_theme_advanced(pixmap_themes[7])
        # print(self.root.get_themes())
        sh = ttk.Separator(root, orient=HORIZONTAL)
        sh.grid(row=2, column=1, columnspan=3, sticky="we")

        # 背景图片
        # self.bg = ImageTk.PhotoImage(file='bg.jpeg')
        bg = Label(self.root, bg='#fff').place(x=0, y=0, relwidth=1, relheight=1)

        # left image
        self.left = ImageTk.PhotoImage(file='lf.png')
        left = Label(self.root, image=self.left).place(x=-180, y=-50,)

        style = ttk.Style()
        style.configure('TCombobox', padding=[0, 0, 0, 5])
        Label(self.root, text='Register Here', font=("times new roman", 25, 'bold'), fg='#00B0FF').place(x=700, y=50)

        Label(self.root, text='Field Name', font=("times new roman", 20, 'bold'), fg='gray').place(x=700, y=100)
        Label(self.root, text='Type', font=("times new roman", 20, 'bold'), fg='gray').place(x=920, y=100)
        Label(self.root, text='Options', font=("times new roman", 20, 'bold'), fg='gray').place(x=1100, y=100)

        # -------Register Frame
        frame = Frame(self.root)
        frame.place(x=700, y=130, width=500, height=400)

        canvas = Canvas(frame, bg='#fff', width=500, height=500, scrollregion=(0, 0, 1000, 1000))

        # hbar = Scrollbar(frame, orient=HORIZONTAL)
        # hbar.pack(side=BOTTOM,fill=X)
        # hbar.config(command=canvas.xview)
        vbar = Scrollbar(frame, orient=VERTICAL, )
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=canvas.yview, )
        canvas.config(width=300, height=300)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side=LEFT, expand=True, fill=BOTH)  # side=LEFT, expand=True, fill=BOTH


        # img2 = PhotoImage("entryBorder", data="""
        #         R0lGODlhHQAdAOMNAAAAAAQGCAgLERkfLR0mODBFZTFFZTNIajtTezxTez1XgD5XgU
        #         Fch////////////ywAAAAAHQAdAAAEbHCQg5i9OGt0iFRaKGLKxBgCoK5s6woGc4Cp
        #         a9+AwFQM7ruYn1AVHP6KRhwyaVsyW87nKioFUKXXZ5a5TXaN32FYOD5eqsAzmlX2tZ
        #         XqNZGxYATkgAD9wCjUqgIFMgR1I4YZCx4TCYeGCR0DEQA7""")
        # style.element_create("blueborder", "image", "entryBorder",
        #                        border=3, sticky="nsew")
        # style.layout("OEntryStyle.TEntry",
        #                [('Entry.blueborder', {'children': [(
        #                    'Entry.padding', {'children': [(
        #                        'Entry.textarea', {'sticky': 'nswe'})],
        #                        'sticky': 'nswe'})], 'sticky': 'nswe'})])
        # style.configure("OEntryStyle.TEntry",
        #                   background="gray",
        #                   foreground="gray")



        # ----------Row 1---------
        # input_text_1 = StringVar() # textvariable=input_text_1,
        self.field1 = ttk.Entry(frame, font=('times new roman', 20)) # FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT
        self.type1 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly',
                             justify=CENTER, values=('1/车类型'),style='TCombobox')
        # ----------Row 2----------
        self.field2 = ttk.Entry(frame, font=('times new roman', 20),  )
        self.type2 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 3----------
        self.field3 = ttk.Entry(frame, font=('times new roman', 20),   )
        self.type3 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 4----------
        self.field4 = ttk.Entry(frame, font=('times new roman', 20),   )
        self.type4 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 5----------
        self.field5 = ttk.Entry(frame, font=('times new roman', 20),   )
        self.type5 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 6----------
        self.field6 = ttk.Entry(frame, font=('times new roman', 20),   )
        self.type6 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 7----------
        self.field7 = ttk.Entry(frame, font=('times new roman', 20))
        self.type7 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 8----------
        self.field8 = ttk.Entry(frame, font=('times new roman', 20), background='pink')
        self.type8 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 9----------
        self.field9 = ttk.Entry(frame, font=('times new roman', 20), )
        self.type9 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 10----------
        self.field10 = ttk.Entry(frame, font=('times new roman', 20), )
        self.type10 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 11----------
        self.field11 = ttk.Entry(frame, font=('times new roman', 20), )
        self.type11 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 12----------
        self.field12 = ttk.Entry(frame, font=('times new roman', 20), )
        self.type12 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 13----------
        self.field13 = ttk.Entry(frame, font=('times new roman', 20), )
        self.type13 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 14----------
        self.field14 = ttk.Entry(frame, font=('times new roman', 20), )
        self.type14 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))

        canvas.create_window(110, 22, window=self.field1)
        canvas.create_window(315, 22, window=self.type1)
        canvas.create_window(110, 60, window=self.field2)
        canvas.create_window(315, 60, window=self.type2)
        canvas.create_window(110, 98, window=self.field3)
        canvas.create_window(315, 98, window=self.type3)
        canvas.create_window(110, 136, window=self.field4)
        canvas.create_window(315, 136, window=self.type4)
        canvas.create_window(110, 174, window=self.field5)
        canvas.create_window(315, 174, window=self.type5)
        canvas.create_window(110, 212, window=self.field6)
        canvas.create_window(315, 212, window=self.type6)

        canvas.create_window(110, 250, window=self.field7)
        canvas.create_window(315, 250, window=self.type7)
        canvas.create_window(110, 288, window=self.field8)
        canvas.create_window(315, 288, window=self.type8)
        canvas.create_window(110, 326, window=self.field9)
        canvas.create_window(315, 326, window=self.type9)
        canvas.create_window(110, 364, window=self.field10)
        canvas.create_window(315, 364, window=self.type10)
        canvas.create_window(110, 402, window=self.field11)
        canvas.create_window(315, 402, window=self.type11)
        canvas.create_window(110, 440, window=self.field12)
        canvas.create_window(315, 440, window=self.type12)
        canvas.create_window(110, 478, window=self.field13)
        canvas.create_window(315, 478, window=self.type13)
        canvas.create_window(110, 516, window=self.field14)
        canvas.create_window(315, 516, window=self.type14)

        # --------- 分割线---------

        # --------- add button --------

        btn = ttk.Button(self.root, text='Download', cursor='hand2', command=self.down)
        btn.place(x=700, y=640, width=150)

        Label(self.root, text='#Rows：', font=("times new roman", 20, 'bold'), fg='gray').place(x=630, y=580)
        qty = ttk.Entry(self.root, font=('times new roman', 20,))
        qty.place(x=706, y=583, width=100)

        Label(self.root, text='Format：', font=("times new roman", 20, 'bold'), fg='gray').place(x=816, y=580)
        save_file_type = ttk.Combobox(self.root, font=('times new roman', 15), state='readonly', justify=CENTER)
        save_file_type['values'] = ('SQL', 'JSON', 'Cassandra CQL')
        save_file_type.place(x=900, y=583, width=120)

        chk = ttk.Checkbutton(self.root, text='include create table', takefocus=0, variable=1)
        chk.place(x=1040, y=585)
        chk.state(['selected'])

    def down(self):
        print('进来了')
        p = self.field1.get()
        l = self.type1.get()

        print(p=='id', l=="1/车类型")

    def add_button(self, i):
        field = Entry(self.root, font=('times new roman', 20),  text=str(i))
        field.place(x=50, y=230, width=200, height=40)
        # field.pack()
        type = ttk.Combobox(self.root, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'),
                            text=str(i))
        type.place(x=255, y=233, width=200, height=35)
        # type.pack()

        b1 = Button(self.root, text='X', command=lambda: self.reduce_button(b1))
        # b1.pack()
        self.button_list.append(field)
        # button_list.append(b)

    def reduce_button(self, b):
        b.destroy()
        if self.button_list:
            b = self.button_list.pop()
            b.destroy()

root = ThemedTk()
obj = App(root)
root.mainloop()