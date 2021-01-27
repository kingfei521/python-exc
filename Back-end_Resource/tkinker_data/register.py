from tkinter import *
import threading
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk
# import tkinter.font as tkfont
# from test import show
# import operator
from comm import File
from template import TEMPLATES
# from comm import *


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
V_list = TEMPLATES







class App(object):
    def __init__(self, root):
        self.root = root
        self.root.title("测试数据生成器")
        self.root.geometry('1250x700+0+0')
        # self.root.resizable(0, 0)
        self.input_queue = []
        self.val = []
        self.root.set_theme_advanced(pixmap_themes[0])
        # print(self.root.get_themes())
        # sh = ttk.Separator(root, orient=HORIZONTAL)
        # sh.grid(row=2, column=1, columnspan=3, sticky="we")
        self.style = ttk.Style()
        self.style.configure('TEntry', selectbackground='#00B0FF')
        # 背景图片
        # self.bg = ImageTk.PhotoImage(file='bg.jpeg')
        bg = Label(self.root, bg='#fff').place(x=0, y=0, relwidth=1, relheight=1)

        # left image
        self.left = ImageTk.PhotoImage(file='lf.png')
        Label(self.root, image=self.left).place(x=-180, y=-50,)

        self.style.configure('TCombobox', padding=[0, 6.5, 0, 6.5], selectbackground='white', selectforeground='black')

        # --------Register
        Label(self.root, text='Register Here', font=("times new roman", 25, 'bold'), fg='#00B0FF').place(x=700, y=50)
        Label(self.root, text='Field Name', font=("times new roman", 20, 'bold'), fg='gray').place(x=700, y=100)
        Label(self.root, text='Type', font=("times new roman", 20, 'bold'), fg='gray').place(x=920, y=100)
        Label(self.root, text='Options', font=("times new roman", 20, 'bold'), fg='gray').place(x=1100, y=100)


        # -------Register Frame
        frame1 = ttk.Frame(self.root) # FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT
        frame1.place(x=700, y=130)


        canvas = Canvas(frame1, bg='#fff', scrollregion=(0, 0, 1000, 1000))  #
        vbar = ttk.Scrollbar(frame1, )
        vbar.pack(side=RIGHT, fill=BOTH)
        vbar.config(command=canvas.yview,)
        canvas.config(width=480, height=415)
        canvas.config(yscrollcommand=vbar.set)
        canvas.pack(side=RIGHT, expand=True, fill=BOTH)  # side=LEFT, expand=True, fill=BOTH



        # ----------Row 1---------
        self.field1 = ttk.Entry(frame1, font=('times new roman', 20)) # FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT
        self.field1.insert(0, 'id')
        self.type1 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list,style='TCombobox')
        self.type1.current(0)
        self.clear1 = ttk.Button(text='X', command=lambda :self.clear(self.field1, self.type1), width=1)
        # ----------Row 2----------
        self.field2 = ttk.Entry(frame1, font=('times new roman', 20),  )
        self.field2.insert(0, 'first_name')
        self.type2 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)
        self.type2.current(1)
        # ----------Row 3----------
        self.field3 = ttk.Entry(frame1, font=('times new roman', 20),   )
        self.field3.insert(0, 'last_name')
        self.type3 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)
        self.type3.current(2)
        # ----------Row 4----------
        self.field4 = ttk.Entry(frame1, font=('times new roman', 20),   )
        self.field4.insert(0, 'email')
        self.type4 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)
        self.type4.current(3)
        # ----------Row 5----------
        self.field5 = ttk.Entry(frame1, font=('times new roman', 20),   )
        self.field5.insert(0, 'gender')
        self.type5 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)
        self.type5.current(4)
        # ----------Row 6----------
        self.field6 = ttk.Entry(frame1, font=('times new roman', 20),   )
        self.field6.insert(0, 'ip_adress')
        self.type6 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)
        self.type6.current(5)
        # ----------Row 7----------
        self.field7 = ttk.Entry(frame1, font=('times new roman', 20))
        self.type7 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)
        # ----------Row 8----------
        self.field8 = ttk.Entry(frame1, font=('times new roman', 20), background='pink')
        self.type8 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)
        # ----------Row 9----------
        self.field9 = ttk.Entry(frame1, font=('times new roman', 20), )
        self.type9 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)
        # ----------Row 10----------
        self.field10 = ttk.Entry(frame1, font=('times new roman', 20), )
        self.type10 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)
        # ----------Row 11----------
        self.field11 = ttk.Entry(frame1, font=('times new roman', 20), )
        self.type11 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)
        # ----------Row 12----------
        self.field12 = ttk.Entry(frame1, font=('times new roman', 20), )
        self.type12 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)
        # ----------Row 13----------
        self.field13 = ttk.Entry(frame1, font=('times new roman', 20), )
        self.type13 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)
        # ----------Row 14----------
        self.field14 = ttk.Entry(frame1, font=('times new roman', 20), )
        self.type14 = ttk.Combobox(frame1, font=('times new roman', 15), state='readonly', justify=CENTER, values=V_list)


# -------------------
        canvas.create_window(110, 22, window=self.field1)
        canvas.create_window(315, 22, window=self.type1)
        canvas.create_window(430, 22, window=self.clear1)
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
# ----------

        # ------------可变 ----------
        name = ttk.Checkbutton(self.root, text='array', takefocus=0, variable=1)
        name.place(x=905, y=575)
        name.state(['selected'])
        name.place_forget()


        entry_1 = ttk.Entry(self.root, width=20, state='disabled')
        entry_1.place(x=700, y=583)
        entry_1.place_forget()

        ttk.Label(self.root, text='#Rows：', font=("times new roman", 20, 'bold')).place(x=500, y=575)
        self.rows = ttk.Entry(self.root, font=('times new roman', 20,))
        self.rows.insert(0, 1000)
        self.rows.place(x=585, y=570, width=100)

        ttk.Label(self.root, text='Format：', font=("times new roman", 20, 'bold')).place(x=690, y=575)
        self.save_file_type = ttk.Combobox(self.root, font=('times new roman', 15), state='readonly', justify=CENTER,
                                           )
        self.save_file_type['values'] = ('JSON', 'SQL', 'CSV')
        # self.save_file_type.current(0)
        self.save_file_type.place(x=780, y=570, width=120)
        self.save_file_type.bind('<<ComboboxSelected>>', self.callback)




        # # ------Download button--------
        btn = ttk.Button(self.root, text='Download', cursor='hand2', command=self.down)
        btn.place(x=1040, y=600, width=150)  # x=1040, y=640,


        self.input_queue.extend([(self.field1, self.type1),
                                (self.field2, self.type2),
                                (self.field3, self.type3),
                                (self.field4, self.type4),
                                (self.field5, self.type5),
                                (self.field6, self.type6),
                                (self.field7, self.type7),
                                (self.field8, self.type8),
                                (self.field9, self.type8),
                                (self.field10, self.type10),
                                (self.field11, self.type11),
                                (self.field12, self.type12),
                                (self.field13, self.type13),
                                (self.field14, self.type14)]
                               )




    def callback(self, event):  # 905 575
        #
        if event.widget.get() == "JSON":
            self.clear()
            a = self.add_radio(self.root, 'array', 905, 575)
            self.val.append(a)
        elif event.widget.get() == "SQL":
            self.clear()
            a = self.add_entry()
            self.val.append(a)

    def clear(self):
        if len(self.val) > 0:
            for i in self.val:
                i.destroy()



    def down(self):
        save_field = {}

        for obj in self.input_queue:
            if obj[0].get() and obj[1].get():
                '''利用faker库,生成数据写入相应的文件'''

                save_field[obj[0].get()] = obj[1].get()

        rows = self.rows.get()
        down_type = self.save_file_type.get()
        select = self.val[-1]

        try:
            if rows:
                if down_type == 'JSON':
                    if len(select.state()) > 0:
                        File("MOCK_DATA").save_data_json(rows, save_field)  # 保存为json
                elif down_type == 'SQL':
                    print(select.get())

        except ValueError as e:
            messagebox.showwarning(title='错误', message='Row is not number or 0: {}'.format(e))




    def add_entry(self):
        field = ttk.Entry(self.root, font=('times new roman', 20))  # FLAT、SUNKEN、RAISED、GROOVE、RIDGE。默认为 FLAT
        field.insert(0, 'MOCK_DATA')
        field.place(x=706, y=640, width=100)
        return field

    def add_radio(self, name, text, x, y):
        name = ttk.Checkbutton(self.root, text=text, takefocus=0, variable=1)
        name.place(x=x, y=y)
        name.state(['selected'])
        return name
    #
    # def clear(self, widget, sel_widget):
    #     widget.delete(0, END)
    #     sel_widget.delete(0, END)

if __name__ == '__main__':

    root = ThemedTk()


    obj = App(root)



    root.mainloop()