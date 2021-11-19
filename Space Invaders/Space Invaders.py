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

# ===ИГРОК===============================================
playerTexture = PhotoImage(file=f"image/player.png")
player = None
playerSpeed = None

LEFTKEY = 0
RIGHTKEY = 1
cnv.bind("<Left>", lambda e, x=LEFTKEY: move(x))
cnv.bind("<Right>", lambda e, x=RIGHTKEY: move(x))
cnv.bind("<space>", lambda e, shoot())
cnv.bind("<Escape>", lambda e, showMenu())

invadersRocketTexture = PhotoImage(file=f"image/rocket/rocket_invaders.png")
invadersRocket = None
invadersRocketSpeedScale = 1.05
invadersRocketSpeedDefault = 1
invadersRocketSpeed = invadersRocketSpeedDefault

rocketsFiles = ["rocket01.png", "rocket02.png", "rocket03.png", "rocket04.png"]
rocketTexture = []
for fileName in rocketsFiles:
    rocketTexture.append(PhotoImage(file=f"image/rocket/{fileName}"))

rocketObject = None
rocketSpeedDefault = 8
rocketSpeedY = rocketSpeedDefault
rocketScale = 1.05

# ===ТЕКСТУРА ВЗРЫВА====================================
explosionFiles = ["expl01.png", "expl02.png", "expl03.png", "expl04.png", "expl05.png", "expl06.png", "expl07.png", "expl08.png"]
explosionTexture = []
for fileName in explosionFiles:
    explosionTexture.append(PhotoImage(file=f"image/expl/{fileName}"))

level = None
frame = 0

# ===НАСТРОЙКА ИГРОКА====================================
score = 0
penalty = 0
lives = 3
playGame = False
defaultName = "Anonymous"

# ===МЕНЮ ИГРЫ===========================================


root.mainloop()
