from tkinter import *
from random import randint
from tkinter import messagebox

# МЕТОДЫ

# Загружаем слова в список
def getWordsFromFile():

    ret = []                                                     # Переменная список для возвращаемого результата
    try:                                                         # Ставим блок проверки ошибок
        f = open("words.dat", "r", encoding="utf-8")             # Получаем дескриптор
        for l in f.readlines():                                  # Читаем построчно
            l = l.replace("\n", "")                              # Убираем последний символ переноса строки /n в конце слов
            ret.append(l)                                        # Добавляем слово в список
        f.close()                                                # Закрываем файл
    except:                                                      # Что произойдёт в случае ошибки?
        print("Проблема с файлом. Программа прекращает работу.")
        quit(0)
    print(ret)
    return ret                                                   # Возвращаем список

# Возвращаем максимальное значение очков из файла
def getTopScore():
    try:
        f = open("topchik.dat", "r", encoding="utf-8")
        m = int(f.readline())
        f.close()
    except:
        m = 0
    return m

# Сохраняем в файл очки пользователя
def saveTopScore():
    global topScore                                              # Обязательно global чтобы можно было изменить topScore
    topScore = score
    try:
        f = open("topchik.dat", "w", encoding="utf-8")
        f.write(str(topScore))
        f.close()
    except:
        messagebox.showinfo("Возникла проблема с файлом при сохранении очков")

# Начало нового раунда
def startNewRound():                # Формируем информацию в окне
    global wordStar, wordComp, userTry
    wordComp = dictionary[randint(0, len(dictionary) - 1)]           # Загадываем слово

    wordStar = "*" * len(wordComp)  # Формируем строку из *
    wordLabel["text"] = wordStar    # Устанавливаем зазвёздленную переменную в метку

    wordLabel.place(x = WIDTH // 2 - wordLabel.winfo_reqwidth() // 2, y = 50)   # Центруем метку в зависимости от слова

    for i in range(33):
        btn[i]["text"] = chr(st + i - 47 * (i // 32))
        btn[i]["state"] = "normal"

    userTry = 10

    updateInfo()                    # Обновляем информацию в окне

# Сравниваем строки и считаем сколько символов различаются
def compareWord(s1, s2):
    res = 0                                                   # Возвращаемый результат
    for i in range(len(s1)):                                  # Сравниваем s1 и s2 посимвольно
        if (s1[i] != s2[i]):                                  # Если символы разные(* поменялась на символ)
            res += 1                                          # Увеличиваем res
    return res

# Возвращаем слово с открытыми символами (Обнаружение символов методом перебора)
def getWordStar(ch):
    ret = ""                        # Переменная для результата

    for i in range(len(wordComp)):  # Перебираем по символам загаданое слово
        if (wordComp[i] == ch):     # Сравниваем символы
            ret += ch               # Добавляем символ в переменную ret если он совпадает
        else:
            ret += wordStar[i]      # Добавляем * в переменную ret если символ не совпадает
    return ret

# При нажатии мышкой на кнопку
def pressLetter(n):
    global wordStar, score, userTry        # Добавляем global чтобы с переменной wordStar можно было работать глобально
    if (btn[n]["text"] == "#"):            # Проверяем если эта буква уже была выбрана, то прерываем метод.
        return 0
    btn[n]["text"] = "#"
    btn[n]["state"] = "disable"

    oldWordStar = wordStar                                    # Временная переменная
    wordStar = getWordStar(chr(st + n - 47 * (n // 32)))      # Получаем строку с открытыми символами
    count = compareWord(wordStar, oldWordStar)                # Находим различие между старой и новой строкой
    wordLabel["text"] = wordStar

    if (count > 0):
        score += count * 5
    else:
        score -= 5
        if (score < 0):
            score = 0

        userTry -= 1

    updateInfo()                            # Обновляем информацию в окне

    if (wordComp == wordStar):              # Если все звёзды раскрыты, то победа
        score += score // 2                 # Добавляем 50% очков
        updateInfo()                        # Обновляем информацию в окне

        if (score > topScore):
            messagebox.showinfo("Поздравляем!", f"Вы - топчик! Угадано слово: {wordComp}! Нажмите OK для продолжения игры.")
            saveTopScore()                  # Метод который записывает рекорд в файл
        else:
            messagebox.showinfo("Отлично", f"Угадано слово: {wordComp}! Нажмите OK для продолжения игры.")

        startNewRound()
    elif (userTry <= 0):
        messagebox.showinfo("Усё!", "Отведённое кол-во попыток закончилось... возвращайтесь скорее!")
        quit(0)

# Обновляем информацию об очках
def updateInfo():
    scoreLabel["text"] = f"Ваши очки: {score}"
    topScoreLabel["text"] = f"Лучший результат: {topScore}"
    userTryLabel["text"] = f"Осталось попыток: {userTry}"

def pressKey(event):
    if (event.keycode == 187):                              # (+)
        wordLabel["text"] = wordComp                        # Подсматриваем загаданное слово (чит)

    ch = event.char.upper()     # Получаем код нажатого на клавиатуре символа и преобразовываем его к верхнему регистру
    if (len(ch) == 0):
        return 0

    codeBtn = ord(ch) - st      # Определяем порядковый номер нажатого символа в русском алфавите (st - символ А)
    if (codeBtn >= 0 and codeBtn <= 33 or codeBtn == -15): # Добавляем букву Ё (or codeBtn == -15)
        pressLetter(codeBtn)

# ==================================================================================================
# MAIN
# Создание окна
root = Tk()                     # В переменной root хранится ссылка на окно в памяти "root имя окна"
root.bind("<Key>", pressKey)
root.resizable(False, False)    # Запрещаем изменение размеров окна
root.title("Угадай слово")      # Устанавливаем заголовок

WIDTH = 810                     # Ширина окна
HEIGHT = 320                    # Высота окна

SCR_WIDTH = root.winfo_screenwidth()    # Ширина экрана в пикеслях
SCR_HEIGHT = root.winfo_screenheight()  # Высота экрана в пикселях

# Вычислим точку в которой расположим окно на экране
POS_X = SCR_WIDTH // 2 - WIDTH // 2     # Координата по x
POS_Y = SCR_HEIGHT // 2 - HEIGHT // 2   # Координата по у
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")

"""
# Настройка геометрии окна без переменных одной строкой
# root.geometry(f"{810}x{320}+{root.winfo_screenwidth() // 2 - 810 // 2}+{root.winfo_screenheight() // 2 - 320 // 2}")
"""

# Метка для вывода слова, которое угадываем в текущем раунде
wordLabel = Label(font="consolas 35")

# Метки для отображения текущих очков, рекорда и оставшихся попыток
scoreLabel = Label(font=", 12")
topScoreLabel = Label(font=", 12")
userTryLabel = Label(font=", 12")

# Установка меток в окне
scoreLabel.place(x=10, y=165)
topScoreLabel.place(x=10, y=190)
userTryLabel.place(x=10, y=215)

# Переменные для хранения значений
score = 0                    # Текущие очки
topScore = getTopScore()     # Рекорд игры
userTry = 10                 # Кол-во попыток

# ======================= СПИСКИ - ЭТО МОДЕЛЬ ХРАНЕНИЯ И ОБРАБОТКИ МНОЖЕСТВА ЗНАЧЕНИЙ =================================

st = ord("А")       # Для определения символа на кнопке по коду ( код("А") + i(1) = "Б" ) ( код("А") + i(2) = "В" )
btn = []            # Список кнопок

for i in range(33):
    btn.append(Button(text=chr(st + i - 47 * (i // 32)), width=2, font="consolas 15")) # Добавляем в список получившийся символ
    btn[i].place(x=215 + (i % 11) * 35, y=150 + i // 11 * 50)                          # Выводим и позицианируем в главном окне
    # - 47 * (i // 32) добавляем чтобы вывести символ "Ё" в конце (он идёт не по порядку, поэтому отнимаем от символа "Я" (-47)
    # Вызываем функцию pressLetter через lambda
    btn[i]["command"] = lambda x = i: pressLetter(x)        # btn[i]["command"] = строка определения команды при нажатии

wordComp = ""                       # Определяем глобально загаданное слово
wordStar = ""                       # Определяем глобально слово со звёздочками
dictionary = getWordsFromFile()     # Словарь
startNewRound()                     # Стартуем

root.mainloop()
