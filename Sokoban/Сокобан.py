from tkinter import *
from time import sleep
from winsound import Beep

# ================== НАЧАЛО ПРОГРАММЫ  =============================
# Настраиваем основное окно(размеры, заголовок, расположение)
root = Tk()
root.resizable(False, False)
root.title("Soko_ban v. 1.0001 alpha supreme")
root.iconbitmap("icon/iconi.ico")

WIDTH = 20
HEIGHT = 10
SQUARE_SIZE = 64

POS_X = root.winfo_screenwidth() // 2 - (WIDTH * SQUARE_SIZE) // 2
POS_Y = root.winfo_screenheight() // 2 - (HEIGHT * SQUARE_SIZE) // 2
root.geometry(f"{WIDTH * SQUARE_SIZE + 0}x{HEIGHT * SQUARE_SIZE + 0}+{POS_X}+{POS_Y}")

# Константы для направления движения ("Коды нажатых клавиш")
UPKEY = 0
DOWNKEY = 1
LEFTKEY = 2
RIGHTKEY = 3

# Создаём полотно для вывода графики
cnv = Canvas (root, width=WIDTH * SQUARE_SIZE, height=HEIGHT * SQUARE_SIZE, bg="#373737")
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)
cnv.focus_set()

# Вызываем функцию движения move через клавиши курсора
cnv.bind("<Up>", lambda e, x=UPKEY: move(x))
cnv.bind("<Down>", lambda e, x=DOWNKEY: move(x))
cnv.bind("<Left>", lambda e, x=LEFTKEY: move(x))
cnv.bind("<Right>", lambda e, x=RIGHTKEY: move(x))

moving = True
backGround = PhotoImage(file="image/grass.png")

# Данный список содержит обьекты PhotoImage с загруженными из файлов изображениями
img = []
img.append(PhotoImage(file="image/wall.png"))               # img[0] - изображение стены
img.append(PhotoImage(file="image/box.png"))                # img[1] - изображение ящика
img.append(PhotoImage(file="image/finish.png"))             # img[2] - изображение точки сбора
img.append([])
img[3].append(PhotoImage(file="image/kosoban_up.png"))      # img[3][0] - изображение погрузчика, направленного вверх
img[3].append(PhotoImage(file="image/kosoban_down.png"))    # img[3][1] - изображение погрузчика, направленного вниз
img[3].append(PhotoImage(file="image/kosoban_left.png"))    # img[3][2] - изображение погрузчика, направленного влево
img[3].append(PhotoImage(file="image/kosoban_right.png"))   # img[3][3] - изображение погрузчика, направленного вправо

# Смотрим какие переменные используются в глобальной области (а None намекает, что задаваться значения будут потом)
player = None
boxes = None
finish = None

win = False

btnReset = Button(text="Сбросить поле".upper(), font=("Consolas", "15"), width=20)
btnReset.place(x=10, y=550)
#btnReset["command"] = reset

btnCheat = Button(text="Установить ящики".upper(), font=("Consolas", "15"), width=20)
btnCheat.place(x=10, y=590)
#btnCheat["command"] = goCheat

textTime = None
second = None
level = 1

dataLevel = []  # Указываем что имеется двумерный глобальный список (Вместо [] можно указать None)
timeRun = None  # Обьект для хранения вызова с помощью .after():
#reset()  # Сбрасывает все переменные и подготавливает игровое поле

root.mainloop()  # Запуск
