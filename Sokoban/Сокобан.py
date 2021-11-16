from tkinter import *
from time import sleep
from winsound import Beep

# Центральный код смены уровнней
def reset():
    global moving, second, timeRun
    print("Метод reset()")
    moving = False
    second = -1
    stopTimer()
    getLevel(level)
    clear_setGrass()
    createLevel()
    updateText()

# Загрузка данных уровня
def getLevel(lvl):
    global dataLevel
    print("Метод getLevel()")
    dataLevel = []
    tmp = []

    idx = str(lvl)
    if (lvl < 10):
        idx = f"0{lvl}"

    try:
        f = open(f"levels/level{idx}.dat", "r", encoding="utf-8")
        for i in f.readlines():
            tmp.append(i.replace("\n", ""))
        f.close()
        # Программа загружает все данные в двумерный список из файла .dat как есть с цифрами (0,1,2,3,4) и уже потом форматируется через createLevel()
        for i in range(len(tmp)):
            dataLevel.append([])
            for j in tmp[i]:
                dataLevel[i].append(int(j))
    except:
        print("Не найден файл с данными.")
        quit(0)


# Останавливаем таймер
def stopTimer():
    global timeRun
    if (timeRun != None):
        root.after_cancel(timeRun)
        timeRun = None

# Замостить изображением grass.png всю область окна
def clear_setGrass():
    print("Метод clear_setGrass():")
    cnv.delete(ALL)                         # Полностью отчищаем полотно
    for i in range(WIDTH):                  # 20
        for j in range(HEIGHT):             # 10
            cnv.create_image(SQUARE_SIZE // 2 + i * SQUARE_SIZE, SQUARE_SIZE // 2 + j * SQUARE_SIZE, image=backGround)
         # (32, 32, img),(32, 96, img),(32, 160, img)...(1248, 672, img)  С помощью цикла выводим изображение на экран

# Создание объектов в Canvas
def createLevel():
    print("Метод createLevel()")
    global player, boxes, finish
    player = []
    boxes = []
    finish = []

    for i in range(len(dataLevel)):
        for j in range(len(dataLevel[i])):
            # Если значение в данной координате равно 1 из (0,1,2,3,4) то расчитываем координаты для вывода текстуры стены (img[0])
            if (dataLevel[i][j] == 1):       # (Счётчик j отвечает за координату x) (Счётчик i отвечает за координату y)
                cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE, SQUARE_SIZE // 2 + i * SQUARE_SIZE, image=img[0])
            elif (dataLevel[i][j] == 3):
                dataLevel[i][j] = 0
                # Информационный объект - список finish (Точки сбора ящиков)
                finish.append([i, j, cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE, SQUARE_SIZE // 2 + i * SQUARE_SIZE, image=img[2]), False])

    # Проверяем файл уровня.dat на наличие значений 2(Ящик), 4(Погрузчик)
    # Второй цикл нужен для того, чтобы погрузчик и ящики гарантированно прорисовывались поверх точек сбора
    for i in range(len(dataLevel)):
        for j in range(len(dataLevel[i])):
            if (dataLevel[i][j] == 2):
                dataLevel[i][j] = 0
                # Информационный объект - список boxes (Ящики)
                boxes.append([i, j, cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE, SQUARE_SIZE // 2 + i * SQUARE_SIZE, image=img[1])])
            elif (dataLevel[i][j] == 4):
                dataLevel[i][j] = 0
                # Информационный объект - список player (Погрузчик)             image=img[3][1] - это изображение погрузчика направленного вниз
                # i - x, j - y => т.е координаты | cnv.create_image => ID объекта(player) на Canvas
                player.append([i, j, cnv.create_image(SQUARE_SIZE // 2 + j * SQUARE_SIZE, SQUARE_SIZE // 2 + i * SQUARE_SIZE, image=img[3][1])])
    print(finish)
    print(player)
    print(boxes)

# Прошедшее время с начала уровня (Данная функция преобразовывает секунды => в "минуты и секунды") 190секунд = 03минуты и 10секунд
def getMinSec(s):
    intMin = s // 60                  # Инициализируем минуты (1 // 60 = 0, 2 // 60 = 0 ...)
    intSec = s % 60                   # Инициализируем секунды (1 % 60 = 1, 2 % 60 = 2 ...)
    textSecond = str(intSec)
    if (intMin > 59):                 # Если например прошло 79 минут
        intMin %= 60                  # 79 % 60 = 19 минут "второго часа"
    if (intSec < 10):                 # Если прошло меньше 10 секунд
        textSecond = "0" + textSecond # Добавляем 0 перед цифрой
    if (intMin == 0):                 # Если прошло 0 минут то просто возвращаем надпись сек.
        return f"{textSecond} сек."
    else:
        textMin = str(intMin)                      # Иначе выводим так же и минуты
        if (intMin < 10):                          # Если меньше 10 минут то выводим 0 перед цифрой по принципу секунд
            textMin = "0" + textMin
        return f"{textMin} мин. {textSecond} сек." # В конце функция возвращает минуты и секунды

# Обновляем полоску с текстом вверху
def updateText():
    global textTime, second, timeRun
    second += 1
    # После каждого прохода удаляем предыдущую строку с целью избежать информационного мессива состоящего из цифр
    cnv.delete(textTime)
    # После удаления формируем новую строку для вывода и вызываем метод getMinSec с текущим кол-вом секунд аргументом
    txt = f"Уровень: {level}     Прошло времени: {getMinSec(second)}"
    # Основная строка с текстом(anchor="nw" значит текст выравнивается по левому краю)
    textTime = cnv.create_text(10, 10, fill="#F7F668", anchor="nw", text=txt, font="Verdana, 13")
    timeRun = root.after(1000, updateText)


# Проверить клетку на доступность перемещения
def move(v):
    print("Метод move()")
    # Проверяем истинность переменной moving (если истинно значит работает анимация) тогда остнавливаем её через return 0
    if (moving):
        return 0
    # Удаляем предыдущее изображение погрузчика cnv.create_image (у нас их всего 4)
    cnv.delete(player[2])
    # Выводим новое изображение с учётом переменной v (которая принимает значения (0,1,2,3) т.е в какую сторону смотрит погрузчик)
    player[2] = cnv.create_image(SQUARE_SIZE // 2 + player[1] * SQUARE_SIZE, SQUARE_SIZE // 2 + player[0] * SQUARE_SIZE, image=img[3][v])
    x = player[0] # Первому значению списка присваисаем переменую x (чтобы потом не писать player[0] )
    y = player[1] # Второму значению списка присваисаем переменую y (чтобы потом не писать player[1] )
    Beep(625, 10) # Издаём истошный звук при нажатиии на клавишу

    if (v == UPKEY):
        check = getNumber(x - 1, y)                   # Получаем код вышестоящей клетки (0,1,2)
        if (check == 0):                              # Если он равен 0 т.е пустое место
            movePlayerTo(0, -8, 8)                    # Запускаем анимацию перемещения вверх (по 8 пикселей за ход для анимации)
            player[0] -= 1                            # Изменяем координату погрузчика
        elif (check == 2):                            # Иначе если там находится ящик код=2
            nextCheck = getNumber(x - 2, y)           # Получаем код на 2 клетки выше "через ящик"
            if (nextCheck == 0):                      # Если он равен 0 т.е пустое место
                numberBox = getBox(x - 1, y)          # Номер ящика (в списке boxes) расположенного выше погрузчика (по направлению движения)
                movePlayerBoxTo(0, -8, 8, numberBox)  # Запускаем анимацию движения погрузчика на место ящика (вверх) по 8 пикселей за ход
                player[0] -= 1                        # Заменяем координату X погрузчика сделав её равной клетке выше
                boxes[numberBox][0] -= 1              # Изменяем координату X ящика на клетку выше
    elif (v == DOWNKEY):                              # Иначе если нажата клавиша вниз...дальше идут однотипные блоки с изменением координат X, Y
        check = getNumber(x + 1, y)
        if (check == 0):
            movePlayerTo(0, 8, 8)
            player[0] += 1
        elif (check == 2):
            nextCheck = getNumber(x + 2, y)
            if (nextCheck == 0):
                numberBox = getBox(x + 1, y)
                movePlayerBoxTo(0, 8, 8, numberBox)
                player[0] += 1
                boxes[numberBox][0] += 1
    elif (v == LEFTKEY):
        check = getNumber(x, y - 1)
        if (check == 0):
            movePlayerTo(-8, 0, 8)
            player[1] -= 1
        elif (check == 2):
            nextCheck = getNumber(x, y - 2)
            if (nextCheck == 0):
                numberBox = getBox(x, y - 1)
                movePlayerBoxTo(-8, 0, 8, numberBox)
                player[1] -= 1
                boxes[numberBox][1] -= 1
    elif (v == RIGHTKEY):
        check = getNumber(x, y + 1)
        if (check == 0):
            movePlayerTo(8, 0, 8)
            player[1] += 1
        elif (check == 2):
            nextCheck = getNumber(x, y + 2)
            if (nextCheck == 0):
                numberBox = getBox(x, y + 1)
                movePlayerBoxTo(8, 0, 8, numberBox)
                player[1] += 1
                boxes[numberBox][1] += 1

# Определяем что находится в клетке
def getNumber(x, y):
    print("Метод getNumber()")
    for box in boxes:
        if (box[0] == x and box[1] == y):
            return 2
        if (dataLevel[x][y] <= 1):
            return dataLevel[x][y]

# Функция возвращает номер ящика под которым он записан в списке boxes[x][y] важно знать какой именно ящик нужно толкать, их может быть несколько
def getBox(x, y):
    print("Метод getBox()")
    for i in range(len(boxes)):
        if (boxes[i][0] == x and boxes[i][1] == y):
            return i
    return None

# Перемещаем погрузчик на требуемое расстояние
def movePlayerTo(x, y, count):
    global moving
    count -= 1                            # 8 пикселей за ход
    cnv.move(player[2], x, y)

    if (count > 0):
        moving = True
        root.after(20, lambda x=x, y=y, c=count: movePlayerTo(x, y, c))
    else:
        print("Метод movePlayerTo() выполнился")
        moving = False

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
level = 5

dataLevel = []  # Указываем что имеется двумерный глобальный список (Вместо [] можно указать None)
timeRun = None  # Обьект для хранения вызова с помощью .after():
reset()  # Сбрасывает все переменные и подготавливает игровое поле

root.mainloop()  # Запуск
