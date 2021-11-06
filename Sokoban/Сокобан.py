from tkinter import *

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

root.mainloop()