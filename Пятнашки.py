from tkinter import *               # Общий Tkinter
from tkinter import ttk             # Для использования RadioButton
from tkinter import messagebox      # Для использования окон сообщений
from random import randint          # Случайные числа
from winsound import Beep           # Простейший генератор звука
from time import sleep              # Задержка выполнения

# Обновление всех изображений
def updatePictures():
    for i in range(n):
        for j in range(m):
            labelImage[i][j]["image"] = imageBackground[dataImage[i][j]]
    root.update()

# Сброс игрового поля
def resetPictures():
    global dataImage

    startButton["state"] = NORMAL
    resetButton["state"] = DISABLED
    diffCombobox["state"] = "readonly"
    radio01["state"] = NORMAL
    radio02["state"] = NORMAL

    for i in range(n):
        for j in range(m):
            dataImage[i][j] = i * n + j

    dataImage[n- 1][m - 1] = blackImg
    Beep(800, 50)
    Beep(810, 35)

    updatePictures()

# Обмен изображений
def exchangeImage(x1, y1, x2, y2):
    global dataImage, labelImage
    dataImage[x1][y1], dataImage[x2][y2] = dataImage[x2][y2], dataImage[x1][y1]
    labelImage[x1][y1]["image"] = imageBackground[dataImage[x1][y1]]
    labelImage[x2][y2]["image"] = imageBackground[dataImage[x2][y2]]
    root.update() # Обновить изображения в главном окне
    sleep(0.02)    # С задержкой

# Перемешиваем
def shufflePictures(x, y):
    if (diffCombobox.current() < 5):
        count = (2 + diffCombobox.current()) ** 4       # 0 => 16 (действий)   4 => 1296 (действий)
        noDirection = 0

        for i in range(count):                # Кол-во циклов зависит от выбранного уровня сложности
            direction = noDirection           # АЛГОРИТМ ИЗБАВЛЕНИЯ ОТ ПОВТОРЕНИЙ (вверх<=>вниз | вправо<=>влево)
            while (direction == noDirection): # 0 0 | 0 0
                direction = randint(0, 3)     #  1  |  0 (пока не появится другая цифра кроме ноля, while будет замыкаться)
                                              # Т.е не допустима ситуация при которой сходили наверх и вернулись вниз
            # Вниз
            if (direction == 0 and x + 1 < n):  # Проверяем что не выходим за границы при(and) заданном направлении
                exchangeImage(x, y, x + 1, y)   # Вызываем метод exchangeImage для перемещения пустого спрайта
                x += 1
                noDirection = 1
            # Вверх
            elif (direction == 1 and x - 1 >= 0):
                exchangeImage(x, y, x - 1, y)
                x -= 1
                noDirection = 0
            # Вправо
            elif (direction == 2 and y + 1 < m):
                exchangeImage(x, y, x, y + 1)
                y += 1
                noDirection = 3
            # Влево
            elif (direction == 3 and y - 1 >= 0):
                exchangeImage(x, y, x, y - 1)
                y -= 1
                noDirection = 2

    else:
        exchangeImage(n - 1, m - 3, n - 1, m - 2)           # Метод перестановки местами 14 15 (неразрешимая ситуация)
    Beep(1750, 50)

    resetButton["state"] = NORMAL

# Стартуем
def startNewRound():
    diffCombobox["state"] = DISABLED
    startButton["state"] = DISABLED
    radio01["state"] = DISABLED
    radio02["state"] = DISABLED

    Beep(750, 50)

    x = 0
    y = 0
    for i in range(n):
        for j in range(m):
            if(dataImage[i][j] == blackImg):
                x = i
                y = j
    shufflePictures(x, y)

def go(x, y):
    print(x, y)
# ============================= НАЧАЛО ПРОГРАММЫ ==========================================

root = Tk()
root.resizable(False, False)
root.title("Головоломка для отчаянных и прокажённых")
root.iconbitmap("icon/iconi.ico")

# ЦВЕТА
back = "#373737"   # Фон
fore = "#AFAFAF"   # Шрифт

WIDTH = 422
HEIGHT = 720
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
root["bg"] = back


# Кнопка ПОСМОТРЕТЬ СОБРАННОЕ
seeButton = Button(root, text="Посмотреть, как должно быть", width=56)
seeButton.place(x=10, y=620)
# seeButton.bind("<Button-1>", seeStart)       # При нажатии вызываем метод seeStart
# seeButton.bind("<ButtonRelease>", seeEnd)    # Когда отпускаем кнопку вызывается метод seeEnd


# Кнопка СТАРТ
startButton = Button(text="СТАРТ", width=56)
startButton.place(x=10, y=650)
startButton["command"] = startNewRound


# Кнопка СБРОС
resetButton = Button(root, text="Сброс", width=56)
resetButton.place(x=10, y=680)
resetButton["command"] = resetPictures


# Метка для вывода текста с кол-вом сделанных ходов и рекордом текущего уровня
textSteps = Label(root, bg=back, fg=fore)
textSteps.place(x=10, y=550)
textRecord = Label(root, bg=back, fg=fore)
textRecord.place(x=10, y=570)

# Метка сложности
Label(root, bg=back, fg=fore, text="Сложность:").place(x=267, y=550)

# Названия степеней сложности перемешивания
itemDiff = ["Только начал","Немного почитал","Знаю print()","Понял сортировку","Изучил лабиринт","Задонатил!"]

# Выпадающий список
diffCombobox = ttk.Combobox(root, width=20, values=itemDiff, state="readonly")
diffCombobox.place(x=270, y=570)
# diffCombobox.bind("<<ComboboxSelected>>", lambda e: refreshText())
diffCombobox.current(0)         # Значение по умолчанию 0 = "Только начал"

# Радиопереключатели
image = BooleanVar()            # Создаём переменную
image.set(True)                 # Устанавливаем значение
# Создаём радио-кнопку и привязываем к ней переменную image
radio01 = Radiobutton(root, text="Пятнашки", variable=image, value=True, activebackground=back, bg=back, fg="#20E0F3")
radio02 = Radiobutton(root, text="Природа", variable=image, value=False, activebackground=back, bg=back, fg="#05C105")
# radio01["command"] = isCheckImage
# radio02["command"] = isCheckImage
radio01.place(x=150, y=550)
radio02.place(x=150, y=570)


# ============== ИЗОБРАЖЕНИЯ ==========================================================================================

n = 4                           # Размер поля(кол-во спрайтов)
m = 4                           # ----------------------------
pictureWidth = 400              # Размер полного изображения(в пикселях)
pictureHeight = 532             # --------------------------------------
widthPic = pictureWidth / n     # Ширина и высота одного спрайта(в пикселях)
heightPic = pictureHeight / m   # ------------------------------------------

fileName = ["img01.png", "img02.png", "img03.png", "img04.png", "img05.png", "img06.png", "img07.png", "img08.png", "img09.png",
             "img10.png", "img11.png", "img12.png", "img13.png", "img14.png", "img15.png", "img16.png", "black.png"]

imageBackground = []      # Активное изображение
imageBackground01 = []    # Пятнашки
imageBackground02 = []    # Природа

for name in fileName:
    imageBackground01.append(PhotoImage(file="image01/" + name)) # После данной конкатенации получаем image01/img01.png, image01/img02.png ... Пятнашки(спрайты)
    imageBackground02.append(PhotoImage(file="image02/" + name)) # После данной конкатенации получаем image02/img01.png, image02/img02.png ... Природа(спрайты)

blackImg = 16

# Изображение в метку "labelImage[x][y]" берётся как изображение из списка "imageBackground[x]" по индексу "dataImage[x][y]".
imageBackground = imageBackground02          # Устанавливаем набор спрайтов(Пятнашки) по умолчанию       (одномерный список imageBackground[x])
labelImage = []                              # Метки Label                                               (двумерный список labelImage[x][y])
dataImage = []                               # Математическая модель игрового поля                       (двумерный список dataImage[x][y])
copyData = []                                # Копия модели игрового поля "Просмотреть, как должно быть" (двумерный список copyData[x][y])
# Пример: Изображение (спрайт верхний левый угол) labelImage[0][0] = imageBackground[dataImage[0][0]]
# Пример: Изображение (спрайт нижний левый угол)  labelImage[3][0] = imageBackground[dataImage[3][0]]
# Формируем списки
for i in range(n):
    labelImage.append([])
    dataImage.append([])
    copyData.append([])

    for j in range(m):                   # [0][0], [0][1], [0][2], [0][3],     Генерируем ряд чисел
        dataImage[i].append(i * n + j)   # [1][4], [1][5], [1][6], [1][7],     номера "собранной" версии
        copyData[i].append(i * n + j)    # [2][8], [2][9], [2][10], [2][11],
                                         # [3][12], [3][13], [3][14], [3][15]

        labelImage[i].append(Label(root, bg=back))                        # Создаём по 4 виджета(ячейки label) на каждую строку (0,1,2,3)
        labelImage[i][j]["bd"] = 1                                        # Ширина границ (bd = border)
        labelImage[i][j].place(x=10 + j * widthPic, y=10 + i * heightPic) # Размещаем виджеты в окне (используем алгоритм автоматического сдвига)
                                                                          # x (сдвиг вправо) => 10 110 210 310
                                                                          # y (сдвиг вниз)      10 143 276 409
        labelImage[i][j].bind("<Button-1>", lambda e, x=i, y=j: go(x, y)) # Что произойдёт при нажатии на виджет (label)
        labelImage[i][j]["image"] = imageBackground[dataImage[i][j]]      # Устанавливаем изображение (через свойство "image") обьект PhotoImage
        # (lambda e, x=i, y=j: go(x, y))                                  => В метод go(x, y) мы будем передавать только x и y
        # Записав "lambda e" перехватываем обьект Event и помещаем его в переменную "e" но эту переменную никуда не отправляем
        # Иными словами, избавляемся от объекта Event так как он нам не требуется

# Обновляем изображения
resetPictures()

root.mainloop()