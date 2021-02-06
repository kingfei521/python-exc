import math
import tkinter as tk
from tkinter import TclError


def make_round_corners_rect(canvas, x0, y0, x1, y1, ratio=0.2, filled=True, fillcolor=''):
    if x0 > x1:
        x0, x1 = x1, x0
    if y0 > y1:
        y0, y1 = y1, y0

    r = min(x1 - x0, y1 - y0) * ratio

    items = []

    topleft = x0, y0
    tld = x0, y0 + r
    tlr = x0 + r, y0
    item = canvas.create_arc(x0, y0, x0 + 2 * r, y0 + 2 * r, start=90, extent=90, fill='', outline='black',
                             style=tk.ARC)
    items.append(item)

    top_right = x1, y0
    trl = x1 - r, y0
    trd = x1, y0 + r
    item = canvas.create_line(*tlr, *trl, fill='black')
    items.append(item)
    item = canvas.create_arc(x1 - 2 * r, y0, x1, y0 + 2 * r, start=0, extent=90, fill='', outline='black', style=tk.ARC)
    items.append(item)

    bot_right = x1, y1
    bru = x1, y1 - r
    brl = x1 - r, y1
    item = canvas.create_line(*trd, *bru, fill='black')
    items.append(item)
    item = canvas.create_arc(x1 - 2 * r, y1 - 2 * r, x1, y1, start=270, extent=90, fill='', outline='black',
                             style=tk.ARC)
    items.append(item)

    bot_left = x0, y1
    blr = x0 + r, y1
    blu = x0, y1 - r
    item = canvas.create_line(*brl, *blr, fill='black')
    items.append(item)
    item = canvas.create_arc(x0, y1 - 2 * r, x0 + 2 * r, y1, start=180, extent=90, fill='', outline='black',
                             style=tk.ARC)
    items.append(item)
    item = canvas.create_line(*blu, *tld, fill='black')
    items.append(item)

    if filled:
        canvas.create_rectangle(x0 + r, y0, x1 - r, y1, fill=fillcolor, outline='')
        canvas.create_rectangle(x0, y0 + r, x1, y1 - r, fill=fillcolor, outline='')
        canvas.create_oval(x0, y0, x0 + 2 * r, y0 + 2 * r, fill=fillcolor, outline='')
        canvas.create_oval(x1 - 2 * r, y0, x1, y0 + 2 * r, fill=fillcolor, outline='')
        canvas.create_oval(x1 - 2 * r, y1 - 2 * r, x1, y1, fill=fillcolor, outline='')
        canvas.create_oval(x0, y1 - 2 * r, x0 + 2 * r, y1, fill=fillcolor, outline='')

    # items = tuple(items)
    # print(items)
    #
    # for item_ in items:
    #     for _item in items:
    #         canvas.addtag_withtag(item_, _item)
    #
    # return items


if __name__ == '__main__':

    root = tk.Tk()
    canvas1 = tk.Canvas(root, width=150, height=100, bg='gray')
    canvas1.grid(row=0, column=0)
    # canvas1.pack(expand=True, fill=tk.BOTH)



    # TL = 100, 100
    # BR = 400, 200
    # make_round_corners_rect(canvas, *TL, *BR)

    # TL = 100, 300
    # BR = 400, 400
    # make_round_corners_rect(canvas, *TL, *BR, ratio=.3)
    #
    # TL = 300, 50
    # BR = 350, 450
    # that_rect = make_round_corners_rect(canvas, *TL, *BR, ratio=.4)
    # for fragment in that_rect:
    #     canvas.itemconfig(fragment, width=4)
    #     try:
    #         canvas.itemconfig(fragment, outline='blue')
    #     except TclError:
    #         canvas.itemconfig(fragment, fill='blue')
    #
    # TL = 150, 50
    # BR = 200, 450
    # make_round_corners_rect(canvas, *TL, *BR, ratio=.07)

    # TL = 30, 30
    # BR = 470, 470
    # that_rect = make_round_corners_rect(canvas, *TL, *BR, ratio=.3)
    # for fragment in that_rect:
    #     canvas.itemconfig(fragment, dash=(3, 3))

    canvas2 = tk.Canvas(root, width=150, height=100, bg='gray')
    canvas2.grid(row=0, column=1)
    TL = 5, 5
    BR = 150, 100
    make_round_corners_rect(canvas1, *TL, *BR, ratio=.1, fillcolor='red')

    TL = 5, 5
    BR = 150, 100
    make_round_corners_rect(canvas2, *TL, *BR, ratio=.1, fillcolor='white')



    root.mainloop()