#       Casino 678
from ctypes import *
import time
import random

valuta = " ₪"
money = 0
playGame = True
defaultMoney = 10000

# windll.Kernel32.GetStdHandle.restype = c_ulong
# h = windll.Kernel32.GetStdHandle(c_ulong(0xfffffff5))

# Вывод сообщения о выигрыше

def pobeda(result):
    color(14)
    print(f"   Победа за тобой! Выигрыш составил: {result}{valuta}")
    print(f"   У тебя на счету: {money}")


# Вывод сообщения о проигрыше

def proigr(result):
    color(12)
    print(f"    К сожалению, проигрыш: {result}{valuta}")
    print(f"    У тебя на счету: {money}")
    print("    Обязательно нужно отыграться!")

# Функция подсчёта совпадений однорукого бандита (3)

def getMaxCount(digit, v1, v2, v3, v4, v5):
    ret = 0
    if (digit == v1):
        ret += 1
    if (digit == v2):
        ret += 1
    if (digit == v3):
        ret += 1
    if (digit == v4):
        ret += 1
    if (digit == v5):
        ret += 1
    return ret

# Анимация однорукого бандита (3)

def getOHBRes(stavka):
    res = stavka

    d1 = 0
    d2 = 0
    d3 = 0
    d4 = 0
    d5 = 0

    getD1 = True
    getD2 = True
    getD3 = True
    getD4 = True
    getD5 = True

    col = 10

    while (getD1 or getD2 or getD3 or getD4 or getD5):
        if (getD1):
            d1 += 1
        if (getD2):
            d2 -= 1
        if (getD3):
            d3 += 1
        if (getD4):
            d4 -= 1
        if (getD5):
            d5 += 1

        if (d1 > 9):
            d1 = 0
        if (d2 < 0):
            d2 = 9
        if (d3 > 9):
            d3 = 0
        if (d4 < 0):
            d4 = 9
        if (d5 > 9):
            d5 = 0

        if (random.randint(0, 20) == 1):
            getD1 = False
        if (random.randint(0, 20) == 1):
            getD2 = False
        if (random.randint(0, 20) == 1):
            getD3 = False
        if (random.randint(0, 20) == 1):
            getD4 = False
        if (random.randint(0, 20) == 1):
            getD5 = False


        time.sleep(0.1)
        color(col)
        col += 1
        if (col > 15):
            col = 10

        # Строка со знаком %, оформление
        print("    " + "%" * 17)
        print(f"    {d1} | {d2} | {d3} | {d4} | {d5}")

    maxCount = getMaxCount(d1, d1, d2, d3, d4, d5)

    if (maxCount < getMaxCount(d2, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d2, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d3, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d3, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d4, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d4, d1, d2, d3, d4, d5)
    if (maxCount < getMaxCount(d5, d1, d2, d3, d4, d5)):
        maxCount = getMaxCount(d5, d1, d2, d3, d4, d5)



    color(14)
    if (maxCount == 2):
        print(f" Совпадение двух чисел! Твой выигрыш в размере ставки: {res}")
    elif (maxCount == 3):
        res *= 2
        print(f" Совпадение трёх чисел! Твой выигрыш 2:1: {res}")
    elif (maxCount == 4):
        res *= 3
        print(f" Совпадение ЧЕТЫРЁХ чисел! Твой выигрыш 5:1: {res}")
    elif (maxCount == 5):
        res *= 10
        print(f" БИНГО! Совпадение всех чисел! Твой выигрыш 10:1: {res}")
    else:
        proigr(res)
        res = 0

    color(11)
    print()
    input(" Нажми Enter для продолжения...")

    return res


# Однорукий бандит (3)

def oneHandBandit():
    global money
    playGame = True

    while (playGame):
        colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ ОДНОРУКОГО БАНДИТА!")
        color(14)
        print(f"\n  У тебя на счету {money}{valuta}\n")
        color(5)
        print(" Правила игры: ")
        print("    1. При совпадении 2-х чисел ставка не списывается.")
        print("    2. При совпадении 3-х чисел выигрыш 2:1.")
        print("    3. При совпадении 4-х чисел выигрыш 5:1.")
        print("    4. При совпадении 5-ти чисел выигрыш 10:1.")
        print("    0. Ставка 0 для завершения игры\n")

        stavka = getIntInput(0, money, f"    Введи ставку от 0 до {money}: ")

        if (stavka == 0):
            return 0
        money -= stavka
        money += getOHBRes(stavka) # возвращает результат игры (выражается в деньгах)положительный либо ноль

        if (money <= 0):
            playGame = False   


# Анимация костей игра  dice (2)

def getDice():
    count = random.randint(3, 8) # Сколько раз перевернутся кубики
    sleep = 0

    while (count > 0):
        color (count + 7)
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        print(" " * 10, "----- -----")
        print(" " * 10, f"| {x} | | {y} |")
        print(" " * 10, "----- -----")

        time.sleep(sleep)
        sleep += 1 / count
        count -= 1

    return x + y

# Кости (2)

def dice():
    global money
    playGame = True

    while (playGame):

        print()
        colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В КОСТИ!")
        color(14)
        print(f"\n У тебя на счету {money}{valuta}\n")

        color(7)
        stavka = getIntInput(0, money, f"    Сделай ставку в пределах {money}{valuta}: ")
        if (stavka == 0):
            return 0


        playRound = True
        control = stavka
        oldResult = getDice()
        firstPlay = True

        while (playRound and stavka > 0 and money > 0):
            if (stavka > money):
                stavka = money
            color(11)
            print(f"\n    В твоём распоряжении {stavka}{valuta}")
            color(12)
            print(f"\n    Текущая сумма чисел на костях: {oldResult}")
            color(11)
            print("\n     Сумма чисел на гранях будет больше, меньше или равна предыдущей?")
            color(7)
            x = getInput ("0123", "    Введи 1 - больше, 2 - меньше, 3 - равна или 0 - выход: ")

            if (x != "0"):
                firstPlay = False
                if (stavka > money):
                    stavka = money

                money -= stavka
                
                # Вызов фукции анимации
                diceResult = getDice()

                win = False # или запись одной строкой от win=(oldResult>diceResult and x=="2")or(oldResult<diceResult and x=="1")

                if (oldResult > diceResult):
                    if (x == "2"):
                        win = True
                elif (oldResult < diceResult):
                    if (x == "1"):
                        win = True
                        # до запись одной строкой
                if (not x == "3"):
                    if (win):
                        money += stavka + stavka // 5
                        pobeda (stavka // 5)
                        stavka += stavka // 5
                    else:
                        stavka = control
                        proigr(stavka)

                elif (x == "3"): # Иначе если пользователь выбрал пункт 3
                    if (oldResult == diceResult):
                        money += stavka * 3
                        pobeda(stavka * 2)
                        stavka *= 3
                    else:
                        stavka = control
                        proigr(stavka)

                oldResult = diceResult

            else:
                # Если выход на первой ставке
                if (firstPlay):
                    money -= stavka
                playRound = False


# Аниммация кручения рулетки и возвращение числа (1)

def getRoulette(visible):
    # Задаем переменные
    tickTime = random.randint(100, 200) / 10000
    mainTime = 0
    number = random.randint(0, 38)
    increaseTickTime = random.randint(100, 110) / 100
    col = 1

    # Главный цикл фукции выполняется пока пауза не станет 0.7 секунды или больше
    while (mainTime < 0.7):
        # Изменение цвета
        col += 1
        if (col > 15):
            col = 1
        # Увелечение времени паузы
        mainTime += tickTime
        tickTime *= increaseTickTime

        # Увелечение номера и вывод на экран
        color(col)
        number += 1
        if (number > 38):
            number = 0
            print()

        # Алгоритм обработки скрытых от пользователя чисел 37, 38 (00, 000)
        printNumber = number
        if (number == 37):
            printNumber = "00"
        elif (number == 38):
            printNumber = "000"

        # Бесподобно эффектный вывод
        print(" Число >", printNumber, "*" * number, " " * (75 - number * 2), "*" * number)

        # Делаем паузу в зависимости от переданного аргумента visible
        if (visible):
            time.sleep(mainTime)


    # Возвращаем выпавшее на рулетке число
    return number



# tickTime - Время в секундах, на которое увеличивается время паузы за однин цикл
# mainTime - Пауза в секундах
# number - Номер выпавший на рулетке
# increaseTickTime - Время в секундах, на которое увеличивается переменная tickTime
# для создания эффекта неравномерности в паузах
# col - Цвет выводимого сообщения

def roulette():
    # Получаем возможность изменения глобальной переменной money
    global money

    # Маркер главного цикла метода рулетки
    playGame = True

    # Главный цикл рулетки
    while (playGame and money > 0):
        colorLine(3, "ДОБРО ПОЖАЛОВАТЬ НА ИГРУ В РУЛЕТКУ!")
        color(14)
        print(f"\n У тебя на счету {money}{valuta}\n")
        color(11)
        print(" Ставлю на...")
        print("    1. Чётное (выигрыш 1:1)")
        print("    2. Нечётное (выигрыш 1:1)")
        print("    3. Дюжина (выигрыш 3:1)")
        print("    4. Число (выигрыш 36:1)")
        print("    0. Возврат в предыдущее меню")

        # Ввод значения: выбор пункта меню
        x = getInput("01234", "    Твой выбор?")

        # Маркер нужно ли нам играть в рулетку?
        playRoulette = True

        # Если игра дюжина то спрашиваем диапазон значений
        if (x == "3"):
            color(2)
            print()
            print(" Выбери числа:...")
            print("    1. От 1 до 12")
            print("    2. От 13 до 24")
            print("    3. От 25 до 36")
            print("    0. Назад")

            # Выбор пункта меню дюжины
            duzhina = getInput("0123", " Твой выбор?")

            # Задаём текст диапазона для вывода в последующем коде
            if (duzhina == "1"):
                textDuzhina = "От 1 до 12"
            elif (duzhina == "2"):
                textDuzhina = "От 13 до 24"
            elif (duzhina == "3"):
                textDuzhina = "От 25 до 36"
            elif (duzhina == "0"):
                playRoulette = False

        # Если играем на число то предоставляем ввод числа        
        elif (x == "4"):
            chislo = getIntInput(0, 36, "    На какое число ставишь? (0...36): ")

        # Если введён ноль в меню рулетки то возвращаемся в основной цикл проги
        color(7)
        if(x == "0"):
            return 0

        # Если продолжаем играть(не введён 0)
        if (playRoulette):
            stavka = getIntInput(0, money, f"     Сколько поставишь? (не больше {money}): ")
            if (stavka == 0):
                return 0
            # Запуск рулетки (если False то сразу получим число без ожидания)
            number = getRoulette(True)

            print()
            color(11)

            # В зависимости от значения number формируем вывод
            if (number < 37):
                print(f"    Выпало число {number}! " + "*" * number)

            else:
                if (number == 37):
                    printNumber = "00"
                elif (number == 38):
                    printNumber = "000"
                print(f"    Выпало число{printNumber}! ")


            # Проверяем ставки и результат
            if (x == "1"):
                print("    Ты ставил на ЧЁТНОЕ!")
                if(number < 37 and number % 2 == 0):
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    proigr(stavka)

            elif (x == "2"):
                print("    Ты ставил на НЕЧЁТНОЕ!")
                if(number < 37 and number % 2 != 0):
                    money += stavka
                    pobeda(stavka)
                else:
                    money -= stavka
                    proigr(stavka)

            elif (x == "3"):
                print(f"    Ставка сделана на диапазон чисел {textDuzhina}.")
                winDuzhina = ""
                if (number > 0 and number < 13):
                    winDuzhina = "1"
                elif (number > 12 and number < 25):
                    winDuzhina = "2"
                elif (number > 24 and number < 37):
                    winDuzhina = "3"

                if (duzhina == winDuzhina):
                    money += stavka * 2
                    pobeda (stavka * 3)
                else:
                    money -= stavka
                    proigr(stavka)

            elif (x == "4"):
                print(f"    Ставка сделана на число {chislo}.")
                if (number == chislo):
                    money += stavka * 35
                    pobeda(stavka * 36)
                else:
                    money -= stavka
                    proigr(stavka)

            # Ждём нажатия Enter и продолжаем
            print()
            input(" Нажми Enter для продолжения...")



# Чтение из файла оставшейся суммы

def loadMoney():
    try:
        f = open("../PythonE/money.dat", "r")
        m = int(f.readline())
        f.close()
    except FileNotFoundError:
        print(f"Файла не существует, задано значение {defaultMoney} {valuta}")
        m = defaultMoney
    return m


# Запись суммы в файл

def saveMoney(moneyToSave):
    try:
        f = open("../PythonE/money.dat", "w")
        f.write(str(moneyToSave))
        f.close()
    except:
        print("Ошибка создания файла, наше Казино закрывается!")
        quit(0)


# Установка цвета текста (win or mac)
# def color(c):
#     windll.Kernel32.SetConsoleTextAttribute(h, c) # Это для windows
def color(c): # Это для mac (pass функция заглушка)
    pass

# Вывод на экран цветного,  обрамлённого звёздочками текста

def colorLine(c, s):
    for i in range(30):
        print()
    color(c)
    print("*" * (len(s) + 2))
    print(" " + s)
    print("*" * (len(s) + 2))
    
# os.system("cls")  # Вначале программы импортируем библиотеку "import os"

# Функция ввода целого числа
def getIntInput(minimum, maximum, message):
    color(7)
    ret = -1
    while (ret < minimum or ret > maximum):
        st = input(message)
        if (st.isdigit()):
            ret = int(st)
        else:
            print("    Введите целое число!")
    return ret


# Функция ввода значения
def getInput(digit, message):
    color(7)
    ret = ""
    while (ret == "" or not ret in digit):
        ret = input(message)
    return ret


# Запуск игры Main Loop
def main():
    global money, playGame

    money = loadMoney()
    startMoney = money

    
    while(playGame and money > 0):
        colorLine(10, "Приветствую тебя в нашем казино, дружище!")
        color(14)
        print(f" У тебя на счету {money}{valuta}")

        color(6)
        print(" Ты можешь сыграть в:")
        print("     1. Рулетку")
        print("     2. Кости")
        print("     3. Однорукого бандита")
        print("     4. Выход. Ставка 0 в играх - выход.")
        color(7)
    

        x = getInput("0123", "    Твой выбор? ")

        if (x == "0"):
            playGame = False
        elif (x == "1"):
            roulette()
        elif(x == "2"):
            dice()
        elif(x == "3"):
            oneHandBandit()



        colorLine(12, "Жаль, что ты покидаешь нас! Но возвращайся скорей!")
        color(13)
        if(money <= 0):
            print("Упс, ты остался без денег. Возьми микрокредит и возвращайся!")

        color(11)
        if(money > startMoney):
            print("Ну что ж, поздравляем с прибылью!")
            print(f"На начало игры у тебя было {startMoney} {valuta}")
            print(f"Сейчас уже {money} {valuta}! Играй ещё и приумножай!")
        else:
            print(f" К сожалению, ты проиграл {startMoney - money} {valuta}")
            print("В следующий раз всё обязательно получится!")

        saveMoney(money)

        color(7)    # Устанавливаем цвет консоли в обычный белый
        quit(0)     # Выход с кодом 0 (можете ставить любое число)


main()        

