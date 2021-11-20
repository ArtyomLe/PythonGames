from tkinter import *
from random import randint
from time import sleep
from winsound import Beep

#============================================================================
# Перемещение игрока
def move(x):
    if (not playGame or onMenu):
        return 0
    if (x == LEFTKEY):
        cnv.move(player[0], -playerSpeed, 0)     # -playerSpeed это на какое кол-во пикселей перемещается игрок налево
    elif (x == RIGHTKEY):
        cnv.move(player[0], playerSpeed, 0)      # playerSpeed это на какое кол-во пикселей перемещается игрок направо
    # Устанавляиваем ограничения чтобы игрок не мог увести корабль за границы окна
    if (getPlayerX() < SQUARE_SIZE):             # По левому краю
        cnv.move(player[0], playerSpeed, 0)
    elif (getPlayerX() > WIDTH - SQUARE_SIZE):   # По правому краю
        cnv.move(player[0], -playerSpeed, 0)

"""

Алгоритм по управлению кораблём игрока *****************************************************************************

1) Создаём одномерный список для хранения данных космического корабля игрока.
2) Устанавливаем вызов метода по нажатии на клавиши влево или вправо.
3) Если игра не началась, или на экране показано меню, то установленный в предыдущем пункте метод не выполняется.
4) Перемещаем текстуру космического корабля, изменяя координаты объекта с помощью .move()
5) Проверяем, выходит ли текстура за границы окна. Если выходит, то перемещаем обратно, в противоположенную сторону.

"""
# Сброс всего подчистую с установкой первого уровня
def globalReset():
    global level, score, penalty, playGame, playerSpeed, lives
    playGame = False
    playerSpeed = 5
    level = 1
    score = 0
    penalty = 0
    lives = 3

# Перезапуск игры полностью
def restartGame():
    globalReset()
    reset()
    showScores(-1)

# Сброс и формирование объектов игрового мира
def reset()
    global invadersObject, invadersWidth, invadersHeight, invadersSpeed, leftInvadersBorder, rightInvadersBorder, player, maxY, rocketObject, invadersRocket

    cnv.delete(ALL)
    cnv.create_image(WIDTH // 2, HEIGHT // 2, image=backGround)
    cnv.focus_set()

    rocketObject = None
    invadersRocket = None
    invadersSpeed = 3 + level // 5              # Чем выше уровень тем быстрее перемещаются пришельцы

    invadersWidth = (1 + int(level // 3)) * 2
    invadersHeight = 2 + (level // 4)
    if (invadersWidth > 14):                    # Ограничиваем ширину в 14 единиц в независимости от повышения уровня
        invadersWidth = 14
    if (invadersHeight > 8):                    # Ограничиваем высоту в 8 единиц в независимости от повышения уровня
        invadersHeight = 8

    maxY = (invadersHeight - 1) * 10 + SQUARE_SIZE * invadersHeight + SQUARE_SIZE // 2

    invadersObject = []
    for i in range(invadersWidth):
        for j in range(invadersHeight):
            rang = randint(0, level // 8)
            if (rang > 2):
                rang = 2
            posX = SQUARE_SIZE // 2 + (WIDTH // 2 - (invadersWidth * (SQUARE_SIZE + 10)) // 2) + i * SQUARE_SIZE + i * 10
            posY = 20 + j * 10 + j * SQUARE_SIZE
            invadersObject.append([cnv.create_image(posX, posY, image=invadersTexture[rang * 2]), rang])

    leftInvadersBorder = cnv.coords(invadersObject[0][0])[0]
    rightInvadersBorder = cnv.coords(invadersObject[len(invadersObject) - 1][0])[0]

    player = [cnv.create_image(WIDTH // 2, HEIGHT - SQUARE_SIZE * 2, image=playerTexture), 1]

    updateInfoLine()
    mainloop()

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
invadersTexture = []    # Список invadersTexture[] хранит обьекты Photoimage с текстурами инопланетян
for fileName in invadersFile:
    invadersTexture.append(PhotoImage(file=f"image/{fileName}"))

# Инициализация глобальных переменных(для захватчиков)
invadersObject = None  # Список ответственный за хранение текстуры и ранга инопланетянина "получает значения в методе reset()"
invadersSpeed = None   # Скорость перемещения инопланетян за один кадр "вычисляется в методе reset()"

leftInvadersBorder = None
rightInvadersBorder = None

maxY = None

invadersWidth = None
invadersHeight = None

# ===ИГРОК===============================================
playerTexture = PhotoImage(file=f"image/player.png")
player = None
playerSpeed = None     # Скорость перемещения игрока за один кадр "задаётся в globalReset()"

LEFTKEY = 0
RIGHTKEY = 1

cnv.bind("<Left>", lambda e, x=LEFTKEY: move(x))
cnv.bind("<Right>", lambda e, x=RIGHTKEY: move(x))
cnv.bind("<space>", lambda e: shoot())
cnv.bind("<Escape>", lambda e: showMenu())

# Вражеская ракета
invadersRocketTexture = PhotoImage(file=f"image/rocket/rocket_invaders.png")
invadersRocket = None
invadersRocketSpeedScale = 1.05  # Коэфициент ускорения выпущенной ракеты (чем ближе к цели, тем труднее увернуться)
invadersRocketSpeedDefault = 1   # Каждый запуск ракеты сбрасывает значение начальной скорости на 1
invadersRocketSpeed = invadersRocketSpeedDefault

# Ракета игрока
rocketsFiles = ["rocket01.png", "rocket02.png", "rocket03.png", "rocket04.png"]
rocketTexture = []
for fileName in rocketsFiles:
    rocketTexture.append(PhotoImage(file=f"image/rocket/{fileName}"))

rocketObject = None
rocketSpeedDefault = 8   # Начальная скорость выпущенной игроком ракеты выше, нежели скорость вражеской (1:8)
rocketSpeedY = rocketSpeedDefault
rocketScale = 1.05

# ===ТЕКСТУРА ВЗРЫВА====================================
explosionFiles = ["expl01.png", "expl02.png", "expl03.png", "expl04.png", "expl05.png", "expl06.png", "expl07.png", "expl08.png"]
explosionTexture = []
for fileName in explosionFiles:
    explosionTexture.append(PhotoImage(file=f"image/expl/{fileName}"))

level = None     # Переменная для хранения номера уровня
frame = 0        # Переменная для хранения текущего кадра отображения текстур инопланетян

# ===НАСТРОЙКА ИГРОКА====================================
score = 0                   # Очки
penalty = 0                 # Штрафы за промахи
lives = 3                   # Жизни
playGame = False
defaultName = "Anonymous"   # Имя по умолчанию если пользователь не захочет вводить свой ник или оставит поле ввода пустым

# ===МЕНЮ ИГРЫ===========================================
menu1 = Button(root, text="Старт", font=", 20", width=20)
menu1.place(x=-100, y=-100)
menu1["command"] = startGame

menu2 = Button(root, text="Сброс", font=", 20", width=20)
menu2.place(x=-100, y=-100)
menu2["command"] = restartGame  # Перезапуск игры полностью

btnContinueAfterPause = None    # Переменная кнопки "Продолжить  в момент демонстрации окна рекордов"

onMenu = False
playerName = None
scores = loadScores()
textScores = None

informationLine = None

# ===НАЧАЛО===============================================
globalReset()       # Сброс всего подчистую с установкой первого уровня
reset()             # Сброс и формирование объектов игрового мира
playGame = True
mainloop()

root.mainloop()
