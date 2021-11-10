from tkinter import *

# Перемещение квадрата игрока
def move(vector):                # Vektor - направление движения
    if (vector == UPKEY):
        cnv.move(player, 0, -playerSpeed)
    elif (vector == DOWNKEY):
        cnv.move(player, 0, playerSpeed)
    elif (vector == LEFTKEY):
        cnv.move(player, -playerSpeed, 0)
    elif (vector == RIGHTKEY):
        cnv.move(player, playerSpeed, 0)

# Перемещение вражеского круга
def evilMove():
    global evilAfter, vectorX, vectorY
    cnv.move(evil, vectorX, vectorY)

    # Получаем координаты в отдельные переменные
    x = cnv.coords(evil)[0]
    y = cnv.coords(evil)[1]

    # Проверяем если круг ударился о границы окна
    if (x > WIDTH - 32 or x < 32):
        vectorX = -vectorX
    if (y > HEIGHT - 32 or y < 32):
        vectorY = -vectorY

    # Получаем координаты игрока
    xP = cnv.coords(player)[0]
    yP = cnv.coords(player)[1]

    # Если расстояние между координатами меньше диаметра круга, то засчитываем соприкосновение (через Пифагора)
    distance = (abs(x - xP) ** 2 + abs(y - yP) ** 2) ** 0.5

    if(distance < 64):
        root.after_cancel(evilAfter)
    else:
        evilAfter = root.after(30, evilMove)

WIDTH = 640
HEIGHT = 480

root = Tk()
root.geometry(f"{WIDTH}x{HEIGHT}")

# Создаём виджет
cnv = Canvas(root, width=WIDTH, height=HEIGHT)
cnv.config(highlightthickness=0)                  # Без рамки
cnv.place(x=0, y=0)                               # В левом верхнем углу
cnv.focus_set()                                   # Перехват с клавиш

# Загружаем изображения
back = PhotoImage(file="background.png")
evilCircle = PhotoImage(file="circle.png")
playerSquare = PhotoImage(file="square.png")

# Устанавливаем нижним слоем фоновое изображение (В canvas начало координат изображения в центре)
cnv.create_image(WIDTH // 2, HEIGHT // 2, image=back)

# Смещение красного круга
vectorX = 5
vectorY = 5

# Скорость движения квадрата
playerSpeed = 10                  # На сколько пикселей за ход перемещается квадрат пользователя (меньше = медленее)

evil = cnv.create_image(32, 32, image=evilCircle)
player = cnv.create_image(WIDTH // 2, HEIGHT // 2, image=playerSquare)

# Задаём коды кнопок в константах для повышения читаемости кода
UPKEY = 0
DOWNKEY = 1
LEFTKEY = 2
RIGHTKEY = 3

# Назначаем клавиши управления курсором
cnv.bind("<Up>", lambda e, x = UPKEY: move(x))
cnv.bind("<Down>", lambda e, x = DOWNKEY: move(x))
cnv.bind("<Left>", lambda e, x = LEFTKEY: move(x))
cnv.bind("<Right>", lambda e, x = RIGHTKEY: move(x))

# Запускаем движение круга
evilAfter = root.after(30, evilMove)
root.mainloop()