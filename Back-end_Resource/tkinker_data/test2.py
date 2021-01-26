from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk, THEMES


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

azx = ['winxpblue', 'kroc', 'scidpurple', 'adapta', 'black', 'alt', 'arc', 'plastik', 'default', 'scidpink', 'itft1', 'elegance', 'scidmint', 'scidblue', 'scidgreen', 'scidsand', 'yaru', 'aqua', 'aquativo', 'breeze', 'blue', 'scidgrey', 'clearlooks', 'clam', 'ubuntu', 'classic', 'keramik', 'equilux', 'radiance', 'smog']

window = ThemedTk()
window.geometry('400x500+0+0')
print(window.get_themes())
window.set_theme_advanced(pixmap_themes[5])
ttk.Button(window, text="Quit").pack()

window.mainloop()