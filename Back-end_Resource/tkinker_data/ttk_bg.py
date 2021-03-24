
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk
from tkinter import *
"""
所有主题使用方式
ThemedTk(theme="Adapta")
"""
Themes = [
    'adapta',  # 自适应式主题
    'aquativo',  # ?
    'arc',  #
    'black',
    'blue',
    'breeze',
    'clearlooks',
    'elegance',
    'equilux',
    'itft1',
    'keramik',
    'kroc',
    'plastik',
    'radiance',
    'scid themes',
    'smog',
    'winxpblue',
    'yaru'
]
# Window color
window = ThemedTk(theme=Themes[-1])
window.wm_minsize(500, 500)
window.configure(background='pink')


s = ttk.Style()
# Create style.css used by default for all Frames
s.configure('TFrame', background='green')
# Create style.css for the first frame
s.configure('Frame1.TFrame', background='red')
# Create style.css for the second frame
s.configure('Frame2.TFrame', background='blue')

# …………………………

F1 = ttk.Frame(window, style='Frame1.TFrame', height=100, width=100).pack()

# 标签框是一个简单的容器小部件。它的主要目的是充当复杂窗口布局的间隔物或容器
lfr = ttk.Labelframe(window, text='This is a A').pack(fill=BOTH, expand=True)
ttk.Label(lfr, text='Inside the LabelFrame').pack()
# x
bt = ttk.Button(window, text="Quit", command=window.destroy).pack()
mt = ttk.Menubutton(window, text='Menu').pack()
lt = ttk.Label(window, text='Doc').pack()
ttk.Entry(window).pack()
ttk.Checkbutton(window).pack()
ttk.Combobox(window).pack()
ttk.LabeledScale(window).pack()
ttk.Radiobutton(window).pack()
ttk.Progressbar(window).pack()
ttk.Scrollbar(window).pack()
ttk.Scale(window).pack()
#
ttk.Sizegrip(window).pack()
ttk.Spinbox(window).pack()
#
m1 = ttk.Panedwindow(window)
m1.pack(fill=BOTH, expand=1)
left = ttk.Label(m1, text='one')
m1.add(left)
#
"""插入列"""
tree = ttk.Treeview(window)
tree["columns"]=("one","two","three")
"""插入行"""
tree.insert('', 'end', 'widgets', text='Widget Tour')
tree.insert('', 0, 'gallery', text='Applications')
# Treeview chooses the id:
id = tree.insert('', 'end', text='Tutorial')

# Inserted underneath an existing node:
tree.insert('widgets', 'end', text='Canvas')
tree.insert(id, 'end', text='Tree')
tree.pack(side=TOP , fill=X)
#

# ttk.OptionMenu(window).pack()
options = [1,2,3,4]
value = StringVar()
value.set(options[1])

dropdown = ttk.OptionMenu(window, value, *options).pack()
# 选项卡标签
note = ttk.Notebook(window)
F2 = ttk.Frame(window, style='Frame2.TFrame')
note.add(F2, text='Tab-1')
note.pack(expand=True, fill=BOTH)



window.mainloop()