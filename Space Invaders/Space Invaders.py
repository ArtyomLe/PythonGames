from tkinter import *
from random import randint
from time import sleep
from winsound import Beep

#============================================================================

# Создание окна
root = Tk()
root.resizable(False, False)
root.title("Вторжение инопланетян")
root.iconbitmap("icon/icon.ico")
WIDTH = 800
HEIGHT = 480
SQUARE_SIZE = 32

POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="#000000")
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)

backGround = PhotoImage(file="image/background.png")

# ===ИНОПЛАНЕТЯНЕ=======================================
invadersFile = ["inv01.png", "inv01_move.png", "inv02.png", "inv02_move.png", "inv03.png", "inv03_move.png"]
invadersTexture = []
for fileName in invadersFile:
    invadersTexture.append(PhotoImage(file=f"image/{fileName}"))

invadersObject = None
invadersSpeed = None

leftInvadersBorder = None
rightInvadersBorder = None

maxY = None
invadersWidth = None
invadersHeight = None

# ==================================================

root.mainloop()
