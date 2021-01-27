from tkinter import *
from ttkthemes import ThemedTk
from tkinter import ttk
def data():
    for i in range(50):
        ttk.Entry(frame, font=('times new roman', 20), ).grid(row=i,column=1)
        Label(frame,text="my text"+str(i)).grid(row=i,column=1)
        Label(frame,text="..........").grid(row=i,column=2)

# 少了这个就滚动不了
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

root=ThemedTk()
sizex = 800
sizey = 600
posx  = 100
posy  = 100
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

myframe=Frame(root,relief=GROOVE,width=600,height=500,bd=1)
myframe.place(x=300,y=100, width=400, height=400)




canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set,)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((100,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)


data()
root.mainloop()
