
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from random import randint

# ==== МЕТОДЫ =============================================================================

#Установка состояния лошадей и погоды
def setupHorse():
    global state01, state02, state03 , state04
    global weather, timeDay
    global winCoeff01, winCoeff02, winCoeff03, winCoeff04
    global play01, play02, play03, play04
    global reverse01, reverse02, reverse03, reverse04
    global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04

    weather = randint(1, 5)
    timeDay = randint(1, 4)

    state01 = randint(1, 5)
    state02 = randint(1, 5)
    state03 = randint(1, 5)
    state04 = randint(1, 5)

    winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
    winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
    winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
    winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

    # Маркеры ситуаций
    reverse01 = False
    reverse02 = False
    reverse03 = False
    reverse04 = False

    play01 = True
    play02 = True
    play03 = True
    play04 = True

    fastSpeed01 = False
    fastSpeed02 = False
    fastSpeed03 = False
    fastSpeed04 = False

# Победа лошади
def winRound(horse):
    global x01, x02, x03, x04, money

    res = "К финишу пришла лошадь " # Просто строковая переменная (res результат)
    if (horse == 1):
        res += nameHorse01 # res = "К финишу пришла лошадь" + {nameHorse01}
        win = summ01.get() * winCoeff01 # win - Переменная, сумма выигрыша(ставка Х коэффициент)
    elif (horse == 2):
        res += nameHorse02
        win = summ02.get() * winCoeff02
    elif (horse == 3):
        res += nameHorse03
        win = summ03.get() * winCoeff03
    elif (horse == 4):
        res += nameHorse04
        win = summ04.get() * winCoeff04

    if (horse > 0):
        res += f"! Вы выиграли {int(win)} {valuta}. "
        if (win > 0):
            res += "Поздравляем! Средства уже зачислены на Ваш счёт!"
            insertText(f"Этот забег принёс Вам {int(win)} {valuta}.")
        else:
            res += "К сожалению, Ваша лошадь была не правильной. Попробуйте ещё раз!"
            insertText("Делайте ставку! Увеличивайте прибыль!")
        messagebox.showinfo("РЕЗУЛЬТАТ", res)
    else:
        messagebox.showinfo("Всё плохо", "До финиша не дошёл никто. Забег признан не состоявшимся. Все ставки возвращены.")
        insertText("Забег признан несостоявшимся.")
        win = summ01.get() + summ02.get() + summ03.get() + summ04.get()

    money += win
    saveMoney(int(money))

    # Сброс переменных
    setupHorse()

    # Сбрасываем виджеты
    startButton["state"] = "normal"
    stavka01["state"] = "readonly"
    stavka02["state"] = "readonly"
    stavka03["state"] = "readonly"
    stavka04["state"] = "readonly"

    stavka01.current(0)
    stavka02.current(0)
    stavka03.current(0)
    stavka04.current(0)

    # Сбрасываем координаты и перерисовываем
    x01 = 20
    x02 = 20
    x03 = 20
    x04 = 20
    horsePlaceInWindow()

    # Обновляем интерфейс
    refreshCombo(eventObject="")  # Обновляет выпадающие списки и чекбосы
    viewWeather()  # Выводит в чат погоду
    healthHorse()  # Выводит в чат информацию о лошадях
    insertText(f"Ваши средства: {int(money)} {valuta}.")  # Выводит в чат информацию о доступной сумме

    # Закрываем программу если сумма средств на счету меньше 1
    if (money < 1):
        messagebox.showinfo("Стоп!", "На ипподром без средств заходить нельзя!")
        quit(0)

# Финансы
def loadMoney():
    try:
        f = open("money.dat", "r") # Открыть файл с записанной суммой для чтения
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение {defaultMoney} {valuta}")
        m = defaultMoney
    return m

# Запись суммы в файл
def saveMoney(moneyToSave):
    try:
        f = open("money.dat", "w") # Открыть файл с записанной суммой для записи
        f.write(str(moneyToSave))
        f.close()
    except:
        print("Ошибка создания файла, наш ипподром закрывается!")
        quit(0)

# При нажатии на кнопку СТАРТ
def runHorse():
    global money
    startButton["state"] = "disabled"
    stavka01["state"] = "disabled"
    stavka02["state"] = "disabled"
    stavka03["state"] = "disabled"
    stavka04["state"] = "disabled"
    money -= summ01.get() + summ02.get() + summ03.get() + summ04.get()
    moveHorse()

# Движ лошадей
def moveHorse():
    global x01, x02, x03, x04

    if (randint(0, 100) < 20):
        problemHorse()

    # Расчитываем скорость для каждой лошади
    speed01 = (randint(1, timeDay + weather) + randint(1, int((7 - state01)) * 3)) / randint(10, 175)
    speed02 = (randint(1, timeDay + weather) + randint(1, int((7 - state02)) * 3)) / randint(10, 175)
    speed03 = (randint(1, timeDay + weather) + randint(1, int((7 - state03)) * 3)) / randint(10, 175)
    speed04 = (randint(1, timeDay + weather) + randint(1, int((7 - state04)) * 3)) / randint(10, 175)

    multiple = 1.5
    speed01 *= int(randint(1, 2 + state01) * (1 + fastSpeed01 * multiple))
    speed02 *= int(randint(1, 2 + state02) * (1 + fastSpeed02 * multiple))
    speed03 *= int(randint(1, 2 + state03) * (1 + fastSpeed03 * multiple))
    speed04 *= int(randint(1, 2 + state04) * (1 + fastSpeed04 * multiple))

    # Вправо или влево бежит лошадь?
    if (play01):
        if (not reverse01):
            x01 += speed01
        else:
            x01 -= speed01
    if (play02):
        if (not reverse02):
            x02 += speed02
        else:
            x02 -= speed02
    if (play03):
        if (not reverse03):
            x03 += speed03
        else:
            x03 -= speed03
    if (play04):
        if (not reverse04):
            x04 += speed04
        else:
            x04 -= speed04

    horsePlaceInWindow()

    # Текущая ситуация
    allPlay = play01 or play02 or play03 or play04                   # Будет True если ни одна лошадь не движется
    allX = x01 < 0 and x02 < 0 and x03 < 0 and x04 < 0               # Убежали ли все лошади влево за границы экрана
    allReverse = reverse01 and reverse02 and reverse03 and reverse04 # Все движутся в обратном направлении

    if (not allPlay or allX or allReverse):
        winRound(0)
        return 0

    # Если лошади ещё не добежали до финиша, то каждый раз вызываем метод moveHorse
    if (x01 < 952 and x02 < 952 and x03 < 952 and x04 <952):
        root.after(5, moveHorse) # .after() обязательно вызывается от имени главного окна (root)
    else:
        if (x01 >= 952):
            winRound(1)
        elif (x02 >= 952):
            winRound(2)
        elif (x03 >= 952):
            winRound(3)
        elif (x04 >= 952):
            winRound(4)

# Метод генерации случайного события (проблемы лошадей)
def problemHorse():
    global reverse01, reverse02, reverse03, reverse04
    global play01, play02, play03, play04
    global state01, state02, state03, state04
    global fastSpeed01, fastSpeed02, fastSpeed03, fastSpeed04

    # Выбираем лошадь для события
    horse = randint(1, 4)
    maxRand = 10000 # чем выше число тем ниже вероятность события

    if (horse == 1 and play01 == True and x01 > 0):
        if(randint(0, maxRand) < state01 * 5):
            reverse01 = not reverse01 # Маркер движения обратный
            # Сообщаем пользователю(вывод окна)
            messagebox.showinfo("Аааа!", f"Лошадь {nameHorse01} развернулась и бежит в другую сторону!")
        elif (randint(0, maxRand) < state01 * 5):
            play01 = False # Лошадь остановилась
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse01} заржала и скинула жокея!")
        elif (randint(0, maxRand) < state01 * 5 and not fastSpeed01):
            messagebox.showinfo("Великолепно!", f"{nameHorse01} перестала притворяться и ускорилась!")
            # Задаём множитель ускорения
            fastSpeed01 = True

    elif (horse == 2 and play02 == True and x02 > 0):
        if(randint(0, maxRand) < state02 * 5):
            reverse02 = not reverse02
            messagebox.showinfo("Аааа!", f"Лошадь {nameHorse02} развернулась и бежит в другую сторону!")
        elif (randint(0, maxRand) < state02 * 5):
            play02 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse02} заржала и скинула жокея!")
        elif (randint(0, maxRand) < state02 * 5 and not fastSpeed02):
            messagebox.showinfo("Великолепно!", f"{nameHorse02} перестала притворяться и ускорилась!")
            fastSpeed02 = True

    elif (horse == 3 and play03 == True and x03 > 0):
        if(randint(0, maxRand) < state03 * 5):
            reverse03 = not reverse03
            messagebox.showinfo("Аааа!", f"Лошадь {nameHorse03} развернулась и бежит в другую сторону!")
        elif (randint(0, maxRand) < state03 * 5):
            play03 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse03} заржала и скинула жокея!")
        elif (randint(0, maxRand) < state03 * 5 and not fastSpeed03):
            messagebox.showinfo("Великолепно!", f"{nameHorse03} перестала притворяться и ускорилась!")
            fastSpeed03 = True

    elif (horse == 4 and play04 == True and x04 > 0):
        if(randint(0, maxRand) < state04 * 5):
            reverse04 = not reverse04
            messagebox.showinfo("Аааа!", f"Лошадь {nameHorse04} развернулась и бежит в другую сторону!")
        elif (randint(0, maxRand) < state04 * 5):
            play04 = False
            messagebox.showinfo("Никогда такого не было и вот опять", f"{nameHorse04} заржала и скинула жокея!")
        elif (randint(0, maxRand) < state04 * 5 and not fastSpeed04):
            messagebox.showinfo("Великолепно!", f"{nameHorse04} перестала притворяться и ускорилась!")
            fastSpeed04 = True

# Отображение состояния лошадей
def healthHorse():
    insertText(getHealth(nameHorse01, state01, winCoeff01))
    insertText(getHealth(nameHorse02, state02, winCoeff02))
    insertText(getHealth(nameHorse03, state03, winCoeff03))
    insertText(getHealth(nameHorse04, state04, winCoeff04))

# Состояние лошадей в текстовой переменной
def getHealth(name, state, win):
    s = f"Лошадь {name} "
    if (state == 5):
        s += "мучается несварением желудка."
    elif (state == 4):
        s += "плохо спала. Подёргивается веко."
    elif (state == 3):
        s += "сурова и беспощадна."
    elif (state == 2):
        s += "в отличном настроении, покушала хорошо."
    elif (state == 1):
        s += "просто ракета!"

    s += f" ({win}:1)"
    return s

# Вывод погоды (случайные значения погоды и времени суток для вывода в чат)
def viewWeather():
    s = "Сейчас на ипподроме "
    if (timeDay == 1):
        s += "ночь, "
    elif (timeDay == 2):
        s += "утро, "
    elif (timeDay == 3):
        s += "день, "
    elif (timeDay == 4):
        s += "вечер, "

    if (weather == 1):
        s += "льёт сильный дождь."
    elif (weather == 2):
        s += "моросит дождик."
    elif (weather == 3):
        s += "облачно, на горизонте тучи."
    elif (weather == 4):
        s += "безоблачно, ветер."
    elif (weather == 5):
        s += "безоблачно, прекрасная погода!."

    insertText(s)

# Добавление строки в текстовый блок (textDiary - имя нашего текстового поля)
def insertText(s):
    textDiary.insert(INSERT, s + "\n")  # (INSERT)-вставить текст (s) с новой строки (+ "\n")
    textDiary.see(END)

# Расположение лошадей на экране
def horsePlaceInWindow():
    horse01.place(x=int(x01), y=20)     # Выводим в окно лошадь 01 
    horse02.place(x=int(x02), y=100)    # Выводим в окно лошадь 02
    horse03.place(x=int(x03), y=180)    # Выводим в окно лошадь 03
    horse04.place(x=int(x04), y=260)    # Выводим в окно лошадь 04

# Отправляем результат вычитания суммы остальных по отношению к текущей ставок из средств money
# Или просто метод отвечающий за работу с выпадающим списком (Combobox)
def refreshCombo(eventObject):
    summ = summ01.get() + summ02.get() + summ03.get() + summ04.get()
    labelAllMoney["text"] = f"У Вас на счету: {int(money - summ)} {valuta}." # левое нижнее окно средств
    # Переменная summ отвечает за хранение суммы всех чисел указананных в выпадающих списках виджетов Combobox
    stavka01["values"] = getValues(int(money - summ02.get() - summ03.get() - summ04.get()))
    stavka02["values"] = getValues(int(money - summ01.get() - summ03.get() - summ04.get()))
    stavka03["values"] = getValues(int(money - summ02.get() - summ01.get() - summ04.get()))
    stavka04["values"] = getValues(int(money - summ02.get() - summ03.get() - summ01.get()))

    if (summ > 0):          # Включаем кнопку старт если ставка сделана
        startButton["state"] = "normal"
    else:
        startButton["state"] = "disabled"

    if (summ01.get() > 0):  # Подсвечиваем чекбокс1 если сделана ставка
        horse01Game.set(True)
    else:
        horse01Game.set(False)
    if (summ02.get() > 0):  # Подсвечиваем чекбокс2 если сделана ставка
        horse02Game.set(True)
    else:
        horse02Game.set(False)
    if (summ03.get() > 0):  # Подсвечиваем чекбокс3 если сделана ставка
        horse03Game.set(True)
    else:
        horse03Game.set(False)
    if (summ04.get() > 0):  # Подсвечиваем чекбокс4 если сделана ставка
        horse04Game.set(True)
    else:
        horse04Game.set(False)

# Формирование значений выпадающего меню (Combobox)
def getValues(summa):   # summa - это входящий в функцию аргумент (число) которое надо разбить на 10 равных частей
    value = []  # Переменной value будет назначена роль списка
    if(summa > 9):
        for i in range(0, 11):
            value.append(i * (int(summa) // 10)) # append увеличивает список на указанное в скобках значение
    else:       # На случай если нет средств на счету
        value.append(0)
        if(summa > 0):
            value.append(summa)
    return value

root = Tk()

# ==== ЗНАЧЕНИЯ ПЕРЕМЕННЫХ =================================================================

WIDTH = 1024  # Ширина окна программы
HEIGHT = 600  # Высота окна программы


# Позиции лошадей
x01 = 20
x02 = 20
x03 = 20
x04 = 20

# Названия лошадей
nameHorse01 = "Ананас"
nameHorse02 = "Сталкер"
nameHorse03 = "Прожорливый"
nameHorse04 = "Копытце"

# Состояние лошадей (1 - хорошее, 5 - плохое)
state01 = randint(1, 5)
state02 = randint(1, 5)
state03 = randint(1, 5)
state04 = randint(1, 5)

# Коэффициент выигрыша на основе показателя здоровья лошади(чем больнее тем он выше(1.9...4.3))
winCoeff01 = int(100 + randint(1, 30 + state01 * 60)) / 100
winCoeff02 = int(100 + randint(1, 30 + state02 * 60)) / 100
winCoeff03 = int(100 + randint(1, 30 + state03 * 60)) / 100
winCoeff04 = int(100 + randint(1, 30 + state04 * 60)) / 100

# Переменные средств на счету
defaultMoney = 10000
money = 0
valuta = "₪"

# Погода (1 - ливень, 5 - ясно)
weather = randint(1, 5)

# Время суток (1 - ночь, 2 -утро, 3 - день, 4 - вечер)
timeDay = randint(1, 4)

# Маркеры ситуаций
reverse01 = False
reverse02 = False
reverse03 = False
reverse04 = False

play01 = True
play02 = True
play03 = True
play04 = True

fastSpeed01 = False
fastSpeed02 = False
fastSpeed03 = False
fastSpeed04 = False

# ==== ФОРМИРОВАНИЕ ЭЛЛЕМЕНТОВ В ОКНЕ =======================================================

#   Создание главного окна
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2   # Координаты размещения окна по центру
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2 # Координаты размещения окна по центру

root.title("ИППОДРОМ")                               # Устанавливаем заголовок
root.resizable(False, False)                         # Запрещаем изменять размеры окна
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")   # Задаём позицию окна на эране


#   Вывод фона
road_image = PhotoImage(file="../PythonE/road.png") # Загружаем изобрж. фона
road = Label(root, image=road_image)     # Устанавливаем изобрж. в Label
road.place(x=0, y=17)                    # Выводим изобрж. в окно


# Загружаем изображения лошадей и устанавливаем в Label
horse01_image = PhotoImage(file="horse01.png") # Загружаем изображение
horse01 = Label(root, image=horse01_image)     # Устанавливаем в Lable
horse02_image = PhotoImage(file="horse02.png") 
horse02 = Label(root, image=horse02_image)
horse03_image = PhotoImage(file="horse03.png") 
horse03 = Label(root, image=horse03_image)
horse04_image = PhotoImage(file="horse04.png") 
horse04 = Label(root, image=horse04_image)     


# Выводим метод с позициями лошадей на экран
horsePlaceInWindow()    

# Выводим кнопку СТАРТ
startButton = Button(text="СТАРТ", font="arial 20", width=61, background="#37AA37")
startButton.place(x=20, y=370)
startButton["state"] = "disabled"


# Выводим чат с информацией под стартом
textDiary = Text(width=70, height=8, wrap=WORD)
textDiary.place(x=430, y=450)

scroll = Scrollbar(command=textDiary.yview, width=20)
scroll.place(x=990, y=450, height=132)
textDiary["yscrollcommand"] = scroll.set


# Отображение суммы средств на экране через метку Label
money = loadMoney()

if(money <= 0):
    messagebox.showinfo("Стоп!", "На ипподром без средств заходить нельзя!")
    quit(0)
    
labelAllMoney = Label(text=f"Осталось средств: {money}{valuta}", font="Arial 12") 
labelAllMoney.place(x=20, y=565)                                                  


# Текст напротив чекбоксов ===================================================================
labelHorse01 = Label(text="Ставка на лошадь №1")
labelHorse01.place(x=20, y=450)
labelHorse02 = Label(text="Ставка на лошадь №2")
labelHorse02.place(x=20, y=480)
labelHorse03 = Label(text="Ставка на лошадь №3")
labelHorse03.place(x=20, y=510)
labelHorse04 = Label(text="Ставка на лошадь №4")
labelHorse04.place(x=20, y=540)


# Чекбоксы ====================================================================================
horse01Game = BooleanVar()
horse01Game.set(0)
horseCheck01 = Checkbutton(text=nameHorse01, variable=horse01Game, onvalue=1, offvalue=0)
horseCheck01.place(x=150, y=448)
horse02Game = BooleanVar()
horse02Game.set(0)
horseCheck02 = Checkbutton(text=nameHorse02, variable=horse02Game, onvalue=1, offvalue=0)
horseCheck02.place(x=150, y=478)
horse03Game = BooleanVar()
horse03Game.set(0)
horseCheck03 = Checkbutton(text=nameHorse03, variable=horse03Game, onvalue=1, offvalue=0)
horseCheck03.place(x=150, y=508)
horse04Game = BooleanVar()
horse04Game.set(0)
horseCheck04 = Checkbutton(text=nameHorse04, variable=horse04Game, onvalue=1, offvalue=0)
horseCheck04.place(x=150, y=538)

# Запрещаем изменять чекбоксы ==================================================================
horseCheck01["state"] = "disabled"
horseCheck02["state"] = "disabled"
horseCheck03["state"] = "disabled"
horseCheck04["state"] = "disabled"

# Выпадающие списки Combobox
stavka01 = ttk.Combobox(root)
stavka02 = ttk.Combobox(root)
stavka03 = ttk.Combobox(root)
stavka04 = ttk.Combobox(root)

# Задаём атрибут "только чтение"
stavka01["state"] = "readonly"
stavka01.place(x=280, y=450)
stavka02["state"] = "readonly"
stavka02.place(x=280, y=480)
stavka03["state"] = "readonly"
stavka03.place(x=280, y=510)
stavka04["state"] = "readonly"
stavka04.place(x=280, y=540)

# Определяем переменные для хранения значений из Combobox
summ01 = IntVar()
summ02 = IntVar()
summ03 = IntVar()
summ04 = IntVar()

# Привязываем переменные к Combobox
# В них будет храниться выбранное в виджете значение
stavka01["textvariable"] = summ01
stavka02["textvariable"] = summ02
stavka03["textvariable"] = summ03
stavka04["textvariable"] = summ04

stavka01.bind("<<ComboboxSelected>>", refreshCombo)
stavka02.bind("<<ComboboxSelected>>", refreshCombo)
stavka03.bind("<<ComboboxSelected>>", refreshCombo)
stavka04.bind("<<ComboboxSelected>>", refreshCombo)

# Обновляем значения Combobox
refreshCombo("")

# Устанавливаем самое первое значение списка
stavka01.current(0)
stavka02.current(0)
stavka03.current(0)
stavka04.current(0)

# Назначаем метод выполняющийся при нажатии на СТАРТ
startButton["command"] = runHorse

viewWeather()
healthHorse()

# Выводим главное окно в экран
root.mainloop()

