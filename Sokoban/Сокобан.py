from tkinter import *
from time import sleep
from winsound import Beep

# ================== НАЧАЛО ПРОГРАММЫ  =============================
root = Tk()
root.resizable(False, False)
root.title("Soko_ban v. 1.0001 alpha beta supreme")
root.iconbitmap("icon/iconi.ico")

WIDTH = 20
HEIGHT = 10
SQUARE_SIZE = 64

POS_X = root.winfo_screenwidth() // 2 - (WIDTH * SQUARE_SIZE) // 2
POS_Y = root.winfo_screenheight() // 2 - (HEIGHT * SQUARE_SIZE) // 2
root.geometry(f"{WIDTH * SQUARE_SIZE + 0}x{HEIGHT * SQUARE_SIZE + 0}+{POS_X}+{POS_Y}")

UPKEY = 0
DOWNKEY = 1
LEFTKEY = 2
RIGHTKEY = 3

cnv = Canvas (root, width=WIDTH * SQUARE_SIZE, height=HEIGHT * SQUARE_SIZE, bg="#373737")
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)
cnv.focus_set()

root.mainloop()
