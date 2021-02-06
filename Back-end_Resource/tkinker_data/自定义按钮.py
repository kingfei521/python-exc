"""
自定义按钮
"""

import tkinter as tk

root = tk.Tk()

def image(smp, image_path):
    img = tk.PhotoImage(file=image_path)
    img = img.subsample(smp, smp)

    return img

button = tk.Button(root,
                   bd=0,
                   relief=tk.RAISED,
                   compound=tk.CENTER,
                   bg='white',
                   fg='yellow',
                   activeforeground='pink',
                   activebackground='white',
                   font='arial 20',
                   text='Download',
                   # pady=1,
                   # padx=1,
                   width=100,
                   height=100)
img = image(2, r'WechatIMG176.jpg')  # 1=normal , 2=small, 3=smallest
button.config(image=img)
button.pack()
root.mainloop()