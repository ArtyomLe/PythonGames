from tkinter import *
from random import randint

# Создание окна
root = Tk()                     # В переменной root хранится ссылка на окно в памяти
root.resizable(False, False)    # Запрещаем изменение размеров окна
root.title("Угадай слово")      # Устанавливаем заголовок