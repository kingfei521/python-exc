from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk




class App(object):
    def __init__(self, root):
        self.root = root
        self.root.title("生成伪数据")
        self.root.geometry('1250x700+0+0')
        self.root.resizable(0, 0)
        self.button_list = []
        sh = ttk.Separator(root, orient=HORIZONTAL)
        sh.grid(row=2, column=1, columnspan=3, sticky="we")
        # 背景图片
        # self.bg = ImageTk.PhotoImage(file='bg.jpeg')
        bg = Label(self.root, bg='#fff').place(x=0, y=0, relwidth=1, relheight=1)

        # left image
        self.left = ImageTk.PhotoImage(file='lf.png')
        left = Label(self.root, image=self.left).place(x=-180, y=-50,)

        Label(self.root, text='Register Here', font=("times new roman", 25, 'bold'), fg='#00B0FF').place(x=700, y=50)

        Label(self.root, text='Field Name', font=("times new roman", 20, 'bold'), fg='gray').place(x=700, y=100)
        Label(self.root, text='Type', font=("times new roman", 20, 'bold'), fg='gray').place(x=905, y=100)
        Label(self.root, text='Options', font=("times new roman", 20, 'bold'), fg='gray').place(x=1100, y=100)

        # -------Register Frame
        frame = Frame(self.root)
        frame.place(x=700, y=130, width=500, height=400)

        canvas = Canvas(frame, bg='#fff', width=500, height=500, scrollregion=(0, 0, 500, 500))

        # hbar = Scrollbar(frame, orient=HORIZONTAL)
        # hbar.pack(side=BOTTOM,fill=X)
        # hbar.config(command=canvas.xview)
        vbar = Scrollbar(frame, orient=VERTICAL, )
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=canvas.yview, )
        canvas.config(width=300, height=300)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side=LEFT, expand=True, fill=BOTH)  # side=LEFT, expand=True, fill=BOTH

        # ----------Row 1---------
        field1 = Entry(frame, font=('times new roman', 20),  relief=RIDGE) # FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT
        type1 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 2----------
        field2 = Entry(frame, font=('times new roman', 20),  relief=RIDGE)
        type2 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 3----------
        field3 = Entry(frame, font=('times new roman', 20),   relief=RIDGE)
        type3 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 4----------
        field4 = Entry(frame, font=('times new roman', 20),   relief=RIDGE)
        type4 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 5----------
        field5 = Entry(frame, font=('times new roman', 20),   relief=RIDGE)
        type5 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 6----------
        field6 = Entry(frame, font=('times new roman', 20),   relief=RIDGE)
        type6 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 7----------
        field7 = Entry(frame, font=('times new roman', 20),   relief=RIDGE)
        type7 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 8----------
        field8 = Entry(frame, font=('times new roman', 20), relief=RIDGE)
        type8 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 9----------
        field9 = Entry(frame, font=('times new roman', 20), relief=RIDGE)
        type9 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 10----------
        field10 = Entry(frame, font=('times new roman', 20), relief=RIDGE)
        type10 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 11----------
        field11 = Entry(frame, font=('times new roman', 20), relief=RIDGE)
        type11 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 12----------
        field12 = Entry(frame, font=('times new roman', 20), relief=RIDGE)
        type12 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 13----------
        field13 = Entry(frame, font=('times new roman', 20), relief=RIDGE)
        type13 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))
        # ----------Row 14----------
        field14 = Entry(frame, font=('times new roman', 20), relief=RIDGE)
        type14 = ttk.Combobox(frame, font=('times new roman', 15), state='readonly', justify=CENTER, values=('1/车类型'))

        canvas.create_window(110, 22, window=field1)
        canvas.create_window(315, 22, window=type1)
        canvas.create_window(110, 60, window=field2)
        canvas.create_window(315, 60, window=type2)
        canvas.create_window(110, 98, window=field3)
        canvas.create_window(315, 98, window=type3)
        canvas.create_window(110, 136, window=field4)
        canvas.create_window(315, 136, window=type4)
        canvas.create_window(110, 174, window=field5)
        canvas.create_window(315, 174, window=type5)
        canvas.create_window(110, 212, window=field6)
        canvas.create_window(315, 212, window=type6)

        canvas.create_window(110, 250, window=field7)
        canvas.create_window(315, 250, window=type7)
        canvas.create_window(110, 288, window=field8)
        canvas.create_window(315, 288, window=type8)
        canvas.create_window(110, 326, window=field9)
        canvas.create_window(315, 326, window=type9)
        canvas.create_window(110, 364, window=field10)
        canvas.create_window(315, 364, window=type10)
        canvas.create_window(110, 402, window=field11)
        canvas.create_window(315, 402, window=type11)
        canvas.create_window(110, 440, window=field12)
        canvas.create_window(315, 440, window=type12)
        canvas.create_window(110, 478, window=field13)
        canvas.create_window(315, 478, window=type13)
        canvas.create_window(110, 516, window=field14)
        canvas.create_window(315, 516, window=type14)

        # --------- 分割线---------

        # --------- add button --------

        btn = Button(self.root, text='Download', cursor='hand2', font=('times new roman', 20), bg='#00B0FF', bd=5,
                     command=self.down)
        btn.place(x=700, y=640, width=150)

        qty = Entry(self.root, font=('times new roman', 20))
        qty.place(x=700, y=580, width=150, height=35)

        save_file_type = ttk.Combobox(self.root, font=('times new roman', 15), state='readonly', justify=CENTER)
        save_file_type['values'] = ('SQL', 'JSON')
        save_file_type.place(x=870, y=583, width=150)

        chk = Checkbutton(self.root, text='I Agree The Terms & Conditions', onvalue=1, offvalue=0, bg='white',
                          font=('times new roman', 12))
        chk.place(x=1040, y=585)








    def down(self):
        print('Downloading......')

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

root = Tk()
obj = App(root)
root.mainloop()