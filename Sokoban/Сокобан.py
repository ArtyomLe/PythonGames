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

# Прошедшее время с начала уровня (Данная функция преобразовывает секунды => в "минуты и секунды")
def getMinSec(s):
    intMin = s // 60
    intSec = s % 60
    textSecond = str(intSec)
    if (intMin > 59):
        intMin %= 60
    if (intSec < 10):
        textSecond = "0" + textSecond
    if (intMin == 0):
        return f"{textSecond} сек."
    else:
        textMin = str(intMin)
        if (intMin < 10):
            textMin = "0" + textMin
        return f"{textMin} мин. {textSecond} сек."

# Обновляем полоску с текстом вверху
def updateText():
    global textTime, second, timeRun
    second += 1
    # После каждого прохода удаляем предыдущую строку с целью избежать информационного мессива состоящего из цифр
    cnv.delete(textTime)
    # После удаления формируем новую строку для вывода и вызываем метод getMinSec с текущим кол-вом секунд аргументом
    txt = f"Уровень: {level}     Прошло времени: {getMinSec(second)}"
    textTime = cnv.create_text(10, 10, fill="#F7F668", anchor="nw", text=txt, font="Verdana, 15") # Основная строка с текстом
    timeRun = root.after(1000, updateText)


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
