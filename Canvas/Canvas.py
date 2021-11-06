from tkinter import *

def go(vector):
    if (vector == UPKEY):
        cnv.move(player, 0, -2)
        cnv.move(evil, 0, 2)
    elif (vector == DOWNKEY):
        cnv.move(player, 0, 2)
        cnv.move(evil, 0, -2)
    elif (vector == LEFTKEY):
        cnv.move(player, -2, 0)
        cnv.move(evil, 2, 0)
    elif (vector == RIGHTKEY):
        cnv.move(player, 2, 0)
        cnv.move(evil, -2, 0)


WIDTH = 640
HEIGHT = 480

root = Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")                     # Размер основного окна

cnv = Canvas(root, width=WIDTH, height=HEIGHT)         # Создаём виджет Canvas с размерами width & height
cnv.config(highlightthickness=0)                       # Убираем белую рамку вокруг окна Canvas
cnv.place(x=0, y=0)                                    # Устанавливаем в область основного окна без отступа (x=0, y=0)
cnv.focus_set()                                        # Перехват нажатия клавиш с Canvas

back = PhotoImage(file="background.png")               # Загружаем (изображение) как фоновую картинку
cnv.create_image(WIDTH // 2, HEIGHT // 2, image=back)  # Привязываем картинку к левому верхнему углу(изначально она по центру)

evilCircle = PhotoImage(file="circle.png")             # Загружаем красный круг
evil = cnv.create_image(32, 32, image=evilCircle)      # Задаём координаты для размещения и помещаем в переменную(evil)

playerSquare = PhotoImage(file="square.png")                            # Загружаем зелёный квадрат
player = cnv.create_image(WIDTH // 2, HEIGHT // 2, image=playerSquare)  # Создаём переменную player

UPKEY = 0
DOWNKEY = 1
LEFTKEY = 2
RIGHTKEY = 3

cnv.bind("<Up>", lambda e, x = UPKEY: go(x))       # При нажатии на кнопку ВВЕРХ будет вызываться go(0)
cnv.bind("<Down>", lambda e, x = DOWNKEY: go(x))   # При нажатии на кнопку ВНИЗ будет вызываться go(1)
cnv.bind("<Left>", lambda e, x = LEFTKEY: go(x))   # При нажатии на кнопку ВЛЕВО будет вызываться go(2)
cnv.bind("<Right>", lambda e, x = RIGHTKEY: go(x)) # При нажатии на кнопку ВПРАВО будет вызываться go(3)

cnv.focus_set()
root.mainloop()