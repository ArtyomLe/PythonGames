from tkinter import *
from random import randint

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

root.mainloop()
