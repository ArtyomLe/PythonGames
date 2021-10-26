from tkinter import *
from random import randint

# МЕТОДЫ
# При нажатии мышкой на кнопку
def pressLetter(n):
    print(f"Нажата буква {chr(st + n - 47 * (n // 32))}")

# MAIN
# Создание окна
root = Tk()                     # В переменной root хранится ссылка на окно в памяти "root имя окна"
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
score = 0           # Текущие очки
topScore = 1000     # Рекорд игры
userTry = 10        # Кол-во попыток

# ======================= СПИСКИ - ЭТО МОДЕЛЬ ХРАНЕНИЯ И ОБРАБОТКИ МНОЖЕСТВА ЗНАЧЕНИЙ =================================

st = ord("А")       # Для определения символа на кнопке по коду ( код("А") + i(1) = "Б" ) ( код("А") + i(2) = "В" )
btn = []            # Список кнопок

for i in range(33):
    btn.append(Button(text=chr(st + i - 47 * (i // 32)), width=2, font="consolas 15")) # Добавляем в список получившийся символ
    btn[i].place(x=215 + (i % 11) * 35, y=150 + i // 11 * 50)                          # Выводим и позицианируем в главном окне
    # - 47 * (i // 32) добавляем чтобы вывести символ "Ё" в конце (он идёт не по порядку, поэтому отнимаем от символа "Я" (-47)
    btn[i]["command"] = lambda x = i: pressLetter(x)

root.mainloop()
