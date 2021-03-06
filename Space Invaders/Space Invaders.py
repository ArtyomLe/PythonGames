from tkinter import *
from random import randint
from time import sleep
from winsound import Beep

#============================================================================

# Очистить всё и начать игру заново
def continueAfterPause():
    btnContinueAfterPause.destroy() # Удаляем кнопку продолжить
    saveScores(scores)              # Записываем таблицу рекордов в файл
    cnv.delete(ALL)                 # Очищаем окно
    showMenu()                      # Показываем меню
    restartGame()                   # Перезапускаем игру с последующим нажатием на СТАРТ

# Запись очков в файл
def endTableScore(inputWindow, positionPlayer):
    global playerName, scores

    root.deiconify()                            # Возвращаем к жизни главное окно (для взаимодействия с пользователем)
    inputWindow.destroy()                       # Удаляем окно ввода
    playerName = playerName.get()               # Задаём значение playerName
    if (playerName == ""):                      # Проверяем на пустоту
        playerName = defaultName
    scores[positionPlayer][0] = playerName
    continueAfterPause()

# Фильтрация вводимых знаков
def inputNameFilter(event):
    global playerName
    filter = "_0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" # Разрешенные символы для ввода имени
    pN = ""                          # Имя
    for i in playerName.get():
        if (i.upper() in filter):
            pN += i
    if (len(pN) > 20):               # Ограничиваем длинну имени до 20 символов
        pN = pN[0:20]
    elif (pN == ""):                 # Если поле пустое то вводим значение прописанное в defaultName
        pN = defaultName
    playerName.set(pN)               # Установка отфильтрованого имени в виджет

# Окно для ввода имени
def getPlayerName(positionPlayer):
    global playerName

    inputWindow = Toplevel(root) # Формируем окно верхнего уровня (поверх основного)
    inputWindow.grab_set()       # Блокируем работу основного "родительского" окна (переделываем вторичное окно в модальное)

    # Геометрия нового окна
    X_NEW = root.winfo_screenwidth() // 2 - 150
    Y_NEW = root.winfo_screenheight() // 2 - 260
    inputWindow.geometry(f"{300}x{120}+{X_NEW}+{Y_NEW}")
    inputWindow.overrideredirect(True)
    inputWindow.focus_set()

    Label(inputWindow, text="Вы - один из лучших! Введите ник:").place(x=13, y=10)

    playerName = StringVar()
    playerName.set(defaultName)
    newName = Entry(inputWindow, textvariable=playerName, width=45)
    newName.place(x=13, y=40)
    newName.focus_set()
    newName.select_range(0, END)                  # Выделяем содержимое поля ввода
    newName.bind("<KeyRelease>", inputNameFilter) # Привязываем inputNameFilter() к любому нажатию клавиш

    # Кнопка продолжить
    btnGo = Button(inputWindow, text="Продолжить...", width=38)
    btnGo.place(x=13, y=70)
    btnGo["command"] = lambda  iW=inputWindow, posP=positionPlayer: endTableScore(iW, posP)

# Находим номер игрока с списке лучших
"""
Задача функции определить позицию игрока в таблице рекордов, 
организовать ввод ника (если он не был введён ранее) 
и вернуть номер позиции в таблице
"""
def sortScoreTable(score):
    global scores
    name = playerName
    if (playerName == None):
        name = "Вы"

    scores.append([name, score]) # Добавляем 11 строку в рекорды
    positionPlayer = 10

    # Применяем метод пузырьковой сортировки работающий с конца списка
    for i in range(len(scores) - 1, 0, -1):   # Начинаем с конца и считаем в начало с шагом в -1
        if (scores[i][1] > scores[i - 1][1]): # Если последний больше предыдущего
            scores[i][0], scores[i - 1][0] = scores[i - 1][0], scores[i][0] # Меняем местами Ник
            scores[i][1], scores[i - 1][1] = scores[i - 1][1], scores[i][1] # Меняем местами кол-во очков
            # Смещаем значение для того чтобы верно определить номер занятого игроком места
            positionPlayer -= 1
    del scores[10] # Удаляем десятый (по факту 11) элемент из таблицы рекордов
        # Если игрок позицию меньше 10 и ещё не вводил имя (в данной сессии)
    if (positionPlayer < 10 and playerName == None):
        getPlayerName(positionPlayer)
    return  positionPlayer

# Конец игры
def endGame():
    global playGame, btnContinueAfterPause, score
    playGame = False
    root.focus_set()
    cnv.create_image(WIDTH // 2, HEIGHT // 2, image=backGround)
    cnv.create_text(160, 80, fill="#FFFFFF", anchor="nw", font=f", 22", text=f"КОНЕЦ ИГРЫ. ЛУЧШИЕ ИГРОКИ:")
    score -= penalty
    showScores(sortScoreTable(int(score))) # Аргументом должен стать номер позиции занятый игроком либо число вне диапазона строк
    btnContinueAfterPause = Button(root, text="Продолжить", width=70)
    btnContinueAfterPause.place(x=140, y=HEIGHT - 50)
    btnContinueAfterPause["command"] = continueAfterPause
"""
1. Прекращаем игру
2. Выводим фоновое изображение, тем самым скрывая ранее выведенные объекты
3. Вызываем прорисовку таблицы рекордов
4. Выводим кнопку продолжить
"""

# Геттеры
def getInvadersX(obj):
    return cnv.coords(obj[0])[0]

def getInvadersY(obj):
    return cnv.coords(obj[0])[1]

def getPlayerX():
    return cnv.coords(player[0])[0]

def getPlayerY():
    return cnv.coords(player[0])[1]

def getRocketX():
    return cnv.coords(rocketObject)[0]

def getRocketY():
    return cnv.coords(rocketObject)[1]

# Обновляем ИнфоСтроку
def updateInfoLine():
    global informationLine
    if (informationLine != None):
        for i in informationLine:
            cnv.delete(i)

    informationLine = []
    informationLine.append(cnv.create_text(20, 440, fill="#ABCDEF", anchor="nw", font=f", 12", text=f"ОЧКИ: {int(score)}"))
    informationLine.append(cnv.create_text(170, 440, fill="#ABCDEF", anchor="nw", font=f", 12", text=f"ВРАГИ: {len(invadersObject)}"))
    informationLine.append(cnv.create_text(320, 440, fill="#ABCDEF", anchor="nw", font=f", 12", text=f"ЖИЗНИ: {lives}"))
    informationLine.append(cnv.create_text(480, 440, fill="#ABCDEF", anchor="nw", font=f", 12", text=f"УРОВЕНЬ: {level}"))
    informationLine.append(cnv.create_text(650, 440, fill="#ABCDEF", anchor="nw", font=f", 12", text=f"ШТРАФЫ: -{penalty}"))

# Запись очков в файл
def saveScores(scoresToFile):
    try:
        f = open("scores.dat", "w", encoding="utf-8")
        for sc in scoresToFile:
            f.write(f"{sc[0]} {sc[1]}\n")
        f.close()
    except:
        print("Что-то пошло не так.")

# Загрузка очков из scores.dat (Список содержит имя игрока и кол-во очков)
def loadScores():
    ret = []
    try:
        f = open("scores.dat", "r", encoding="utf-8")
        for sc in f.readlines():
            s = sc.replace("\n", "")
            s = s.split(" ")

            if (len(s[0]) > 20):      # Длинна имени не может быть больше 20 символов
                s[0] = s[0][0:20]     # В случае превышения имя обрезается
            elif (s[0] == ""):        # Если не ввели имя то записываем defaultName
                s[0] = defaultName
            s[1] = int(s[1])          # Второе значение целое число int т.е рекорд
            if (s[1] > 1000000):
                s[1] = 1000000        # Рекорд не может превышать число 1000000
            elif (s[1] < 0):
                s[1] = 0              # В случае 0 => 0
            ret.append(s)
        f.close()
    except:
        print("Файла не существует.")
    if (len(ret) != 10):                  # Если файл состоит не из 10 строк
        ret = []
        for i in range(10):
            ret.append([defaultName, 0])  # Переписываем в defaultName, 0
        saveScores(ret)
    return ret

# Удаление таблицы очков
def hideScores():
    global textScores
    for i in textScores:
        cnv.delete(i)

# Рисуем таблицу очков
def showScores(numberPlayer):
    global textScores
    textScores = []

    for i in range(len(scores)):
        if (i == numberPlayer):
            colorText = "#00FF55"  # Подсвечиваем зелёным если попадаем в список
        else:
            colorText = "#AA9922"  # Всё остальное жёлтым
        # Номер строки
        textScores.append(cnv.create_text(210, 170 + i * 22, fill=colorText, font=", 14", text=str(i + 1)))
        # Ник игрока [0]      (anchor - это координаты в окне)
        textScores.append(cnv.create_text(240, 170 + i * 22, fill=colorText, anchor="w", font=", 14", text=scores[i][0]))
        # Кол-во очков [1]    (anchor - это координаты в окне)
        textScores.append(cnv.create_text(590, 170 + i * 22, fill=colorText, anchor="e", font=", 14", text=scores[i][1]))

# Показываем кнопки меню
def showMenu():
    global menu1, menu2, onMenu
    if (not onMenu):
        menu1.place(x=235, y=37)
        menu2.place(x=235, y=97)
        showScores(-1)
        onMenu = True
    else:
        hideMenu()

# Скрываем кнопки меню, меняя их координаты
def hideMenu():
    global menu1, menu2, onMenu
    if (onMenu):
        menu1.place(x=-100, y=-100)
        menu2.place(x=-100, y=-100)
        onMenu = False
        hideScores() # Скрываем таблицу очков
    else:
        showMenu()

# Анимация полёта вражеской ракеты
def animationInvadersRocket():
    global invadersRocket, invadersRocketSpeed, lives

    if (not playGame):
        invadersRocket = None
        invadersRocketSpeed = invadersRocketSpeedDefault
        return 0

    # Смещаем ракету
    cnv.move(invadersRocket, invadersSpeed / 2, int(invadersRocketSpeed))

    invadersRocketSpeed *= invadersRocketSpeedScale
    # Помещаем координаты ракеты в переменные
    x = cnv.coords(invadersRocket)[0]
    y = cnv.coords(invadersRocket)[1]
    # Расчитываем попадание в игрока
    if (y > getPlayerY() - SQUARE_SIZE // 2): # Если Y ракеты больше чем у игрока (начало координат в верхней левой точке)
        if (x > getPlayerX() - SQUARE_SIZE and x < getPlayerX() + SQUARE_SIZE): # А Х находится между левой и правой границой игрока
            animationExplosion(7, getPlayerX(), getPlayerY()) # Если попали (отрисовка текстуры взрыва с индекса 7 (список explotionTexture))
            Beep(400, 2)
            Beep(550, 2)
            Beep(570, 3)
            y = HEIGHT                                        # Удаляем текстуру чтобы можно было выпустить след. ракету (потому что попали)
            lives -= 1                                        # Отнимаем жизнь
            cnv.coords(player[0], WIDTH // 2, getPlayerY())   # Возвращаем игрока на середину (начальную позицию)

    if (y < HEIGHT):                                          # Повторный запуск ракеты
        root.after(20, animationInvadersRocket)
    else:                                                     # Если ракета не попала и вылетела за границы окна то удаляем её текстуру
        cnv.delete(invadersRocket)
        invadersRocket = None                                 # Задаём скорость по умолчанию
        invadersRocketSpeed = invadersRocketSpeedDefault

# Стартуем ракету врага
def startInvadersRocket():
    global invadersRocket

    if (not playGame):
        return 0

    if (len(invadersObject) > 0):                # Если есть в окне хотя бы один пришелец
        n = randint(0, len(invadersObject) - 1)  # Случайно выбираем пришельца который будет стрелять и помещаем его в переменную n
        Beep(1200, 40)
        invadersRocket = cnv.create_image(getInvadersX(invadersObject[n]), getInvadersY(invadersObject[n]), image=invadersRocketTexture)
        root.after(20, animationInvadersRocket)  # Запускаем анимацию полёта ракеты с интервалом в 20 миллисекунд

# Анимация взрыва
def animationExplosion(frame, x, y):
    if (not playGame):
        return 0
    # Каждый цикл отрисовываем и удаляем фрэйм для эффекта взрыва (всего 0:7)
    tempExpl = cnv.create_image(x, y, image=explosionTexture[frame])
    if (frame > -1):
        root.after(10, lambda frame=frame - 1, x=x, y=y: animationExplosion(frame, x, y))
    cnv.update()
    sleep(0.01 + frame / 1000)
    cnv.delete(tempExpl)

# Старт анимации взрыва пришельца
def startExplosion(n):   # (n) он же (find) Номер конкретного инопланетянина
    global invadersObject
    if (not playGame):
        return 0

    Beep(650, 20)
    animationExplosion(7, getInvadersX(invadersObject[n]), getInvadersY(invadersObject[n]))
    # Уменьшаем ранг пришельца, и проверяем если можно его удалить
    invadersObject[n][1] -= 1
    if (invadersObject[n][1] < 0):       # Если ранг отрицательный то можно удалять
        cnv.delete(invadersObject[n][0])
        del invadersObject[n]

# Анимация полёта ракеты игрока
def animationShoot(frame):
    global rocketObject, rocketSpeedY, penalty, score, player
    if (not playGame):
        rocketObject = None
        rocketSpeedY = rocketSpeedYDefault
        return 0

    cnv.move(rocketObject, 0, -rocketSpeedY)
    rocketSpeedY *= rocketScale

    x = getRocketX()
    y = getRocketY()

    frame += 1
    if (frame > len(rocketTexture) - 1):
        frame = 0
    sleep(0.02)
    cnv.delete(rocketObject)
    rocketObject = cnv.create_image(x, y, image=rocketTexture[frame])

    if (cnv.coords(rocketObject)[1] < maxY + SQUARE_SIZE): # Координата ракеты по Y меньше (т.е находится в прямоугольнике врага)
        rocketX = getRocketX()
        rocketY = getRocketY()
        find = 0                # Сравнение координат ракеты с координатами каждого пришельца

        while (find < len(invadersObject)):
            invadersX = getInvadersX(invadersObject[find])
            invadersY = getInvadersY(invadersObject[find])

            # Чем меньше цифра коэфициента, тем тяжелее попасть
            if (abs(invadersX - rocketX) < SQUARE_SIZE * 0.4 and abs(invadersY - rocketY) < SQUARE_SIZE * 0.8):
                score += 50 * (level + 1)  # При попадании увеличиваем кол-во очков
                startExplosion(find)       # Вызываем метод взрыва
                y = -1                     # Прекращаем вызов метода анимации полёта ракеты animationShoot()
                find = len(invadersObject) # Прекращаем цикл while
                penalty -= 5               # Уменьшаем штрафные очки
            find += 1                          # Продолжаем проверять остальных пришельцев ( если не попали )

    # Y находится в пространстве окна (ракета движется дальше)
    if (y > 0):
        root.after(3, lambda frame=frame: animationShoot(frame))
    else:
        Beep(700, 20)
        cnv.delete(rocketObject)           # Удаляем обьект если он находится за границами окна (ракету)
        penalty += 5                       # Добавляем к штрафному (за промах)
        player[1] += 1                     # Перезаряд
        rocketSpeedY = rocketSpeedYDefault # Скорость ставим на default значение

# Выстрел при нажатии на пробел
def shoot():
    global player, rocketObject

    if (not playGame or onMenu):
        return 0
    if (player[1] == 0):
        return 0
    player[1] -= 1                  # При выстреле уменьшаем заряд с 1 до 0
    rocketObject = cnv.create_image(getPlayerX(), getPlayerY(), image=rocketTexture[0])
    root.after(10, lambda frame=0: animationShoot(frame))

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

# Переключение на следующий уровень
def nextLevel():
    global level, playGame
    cnv.delete(ALL)
    level += 2
    playGame = True
    reset()

# Конец уровня
def endLevel():
    global playGame
    playGame = False
    cnv.delete(ALL)
    cnv.create_text(WIDTH // 2, HEIGHT // 2, fill="#FFFFFF", font=f", 15", text=f"ПОБЕДА! ЗАГРУЖАЕМ СЛЕДУЮЩИЙ УРОВЕНЬ!")

    root.focus_set()
    root.update()
    Beep(randint(850, 1000), 400)
    sleep(0.01)
    Beep(randint(750, 1000), 200)
    sleep(0.03)
    Beep(randint(950, 1000), 600)
    sleep(0.07)
    Beep(randint(850, 1000), 500)
    root.after(300, nextLevel)

# Главный цикл игры
def mainloop():
    global invadersObject, leftInvadersBorder, rightInvadersBorder, invadersSpeed, playGame, score, maxY, frame

    if (len(invadersObject) == 0):      # Проверяем если инопланетяне уничтожены
        endLevel()
    if (not playGame):                  # Если нет игры то прерываем главный цикл
        return 0

    for obj in invadersObject:                    # Перерисовываем текстуры
        cnv.move(obj[0], int(invadersSpeed), 0)   # Смещаем каждого инопланетянина по оси Х на скорость invadersSpeed
        xPos = getInvadersX(obj)                  # Функции getInvadersX,Y созданы для дальнейшего сокращения записи
        yPos = getInvadersY(obj)
        cnv.delete(obj[0])                        # Удаление обьекта с Canvas
        # Создаём объект с новой текстурой на сохранённых координатах
        obj[0] = cnv.create_image(xPos, yPos, image=invadersTexture[obj[1] * 2 + frame])

    frame += 1                                  # Контролируем кол-во кадров, их может быть только два (invadersTexture)
    if (frame > 1):
        frame = 0
    # Условные границы прямоугольника (Левый и Правый)
    # Изменяем на скорость смещения и делаем число целым (из-за ускорения invadersSpeed на 1.1 )
    leftInvadersBorder += int(invadersSpeed)
    rightInvadersBorder += int(invadersSpeed)

    # Вычисляем могут ли пришельцы пульнуть (метод startInvadersRocket)
    if (randint(0, 150) < abs(invadersSpeed) and invadersRocket == None): # Пришельцы движутся и не выпустили ракету
        startInvadersRocket()

    # Проверяеям если не вышли за границу окна (блок инопланетян)
    if (rightInvadersBorder > WIDTH - SQUARE_SIZE or leftInvadersBorder < SQUARE_SIZE): # Если условие верно
        invadersSpeed *= 1.1                  # Ускоряемся
        invadersSpeed = -invadersSpeed        # Инверсируем скорость ( движение в противоположную сторону )
        maxY = 0                              # Поиск максимальной точки Y для всего блока
        for obj in invadersObject:
            cnv.move(obj[0], 0, SQUARE_SIZE)  # Смещаем на расстояние фигурки (32пикселя)
            if (cnv.coords(obj[0])[1] + SQUARE_SIZE // 2 > maxY):
                maxY = cnv.coords(obj[0])[1] + SQUARE_SIZE // 2
    root.after(100, mainloop)
    score -= .1                               # За 10 вызовов в секунду пропадает одно очко
    updateInfoLine()                          # Обновляем информационную строку внизу окна

    if (maxY > getPlayerY() or lives < 0):    # Условия проигрыша
        endGame()

# Нажатие на кнопку СТАРТ
def startGame():
    global playGame
    if (playGame):
        hideMenu()
        return 0
    playGame = True
    hideMenu()
    mainloop()

# Сброс всего подчистую с установкой первого уровня
def globalReset():
    global level, score, penalty, playGame, playerSpeed, lives
    playGame = False
    playerSpeed = 12
    level = 1
    score = 0
    penalty = 0
    lives = 2

# Перезапуск игры полностью
def restartGame():
    globalReset()
    reset()
    showScores(-1)

# Сброс и формирование объектов игрового мира
def reset():
    global invadersObject, invadersWidth, invadersHeight, invadersSpeed, leftInvadersBorder, rightInvadersBorder, player, maxY, rocketObject, invadersRocket

    cnv.delete(ALL)
    cnv.create_image(WIDTH // 2, HEIGHT // 2, image=backGround)
    cnv.focus_set()                             # Обработчик событий (нажатие клавиш)

    rocketObject = None
    invadersRocket = None
    invadersSpeed = 3 + level // 5              # Вычисление горизонтальной скорости перемещения инопланетян(пиксели за ход)

    # Вычисление прямоугольника инопланетян(ШxВ)
    invadersWidth = (1 + int(level // 3)) * 2
    invadersHeight = 2 + (level // 4)

    # Максимальное значение армады 14x8
    if (invadersWidth > 14):                    # Ограничиваем ширину в 14 единиц в независимости от повышения уровня
        invadersWidth = 14
    if (invadersHeight > 8):                    # Ограничиваем высоту в 8 единиц в независимости от повышения уровня
        invadersHeight = 8

    maxY = (invadersHeight - 1) * 10 + SQUARE_SIZE * invadersHeight + SQUARE_SIZE // 2

    invadersObject = []                         # Двумерный список инопланетян
    for i in range(invadersWidth):
        for j in range(invadersHeight):
            rang = randint(0, level // 8)       # После 8 уровня начинают появляться более сложные экземпляры
            if (rang > 2):                      # С максимальной сложностью = 2
                rang = 2
            posX = SQUARE_SIZE // 2 + (WIDTH // 2 - (invadersWidth * (SQUARE_SIZE + 10)) // 2) + i * SQUARE_SIZE + i * 10
            posY = 20 + j * 10 + j * SQUARE_SIZE
            invadersObject.append([cnv.create_image(posX, posY, image=invadersTexture[rang * 2]), rang])

    # Левая и правая границы блока для рассчёта столкновения с границами окна
    leftInvadersBorder = cnv.coords(invadersObject[0][0])[0]
    rightInvadersBorder = cnv.coords(invadersObject[len(invadersObject) - 1][0])[0]

    player = [cnv.create_image(WIDTH // 2, HEIGHT - SQUARE_SIZE * 2, image=playerTexture), 1]

    updateInfoLine() # Обновляем информационный текст внизу экрана
    mainloop()       # Запускаем игру

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
rocketSpeedYDefault = 8            # Начальная скорость выпущенной игроком ракеты выше, нежели скорость вражеской (1:8)
rocketSpeedY = rocketSpeedYDefault # Скорость ракеты по Y
rocketScale = 1.05                # Коэфициент ускорения ракеты выпущенной игроком

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
