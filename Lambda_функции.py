
import time

def gms():
    return int(time.time() % 1 * 1000)
print(gms())

print("\n")
# =======================================

import time

gms = lambda : int(time.time() % 1 * 1000)
print(gms())

print("\n")
# =======================================

from tkinter import *
from random import randint

root = Tk()                     # В переменной root хранится ссылка на окно в памяти "root имя окна"
root.resizable(False, False)    # Запрещаем изменение размеров окна
root.title("Угадай слово")      # Устанавливаем заголовок
root.geometry(f"{810}x{320}+{root.winfo_screenwidth() // 2 - 810 // 2}+{root.winfo_screenheight() // 2 - 320 // 2}")

def pressButton():
    print(lambda : 3 * 5)

myButton = Button(text="Кнопка", width=25)
myButton.place(x=10, y=10)
myButton["command"] = pressButton                   # ["command"] - это свойство которое требует объект

root.mainloop()

print("\n")
# =======================================


def kvadrat(n):
    return n * n
a = []
for i in range(10):
    a.append(lambda x = i: kvadrat(x))

print(a[5]())               # Вывод на экран функции хранящейся в элементе с индексом 5 (не результат а именно функция!)
for i in range(10):
    print(a[i])


# =======================================

from  datetime import datetime, timedelta
def getData():
    return datetime.strftime(datetime.now(), '%d-%m-%Y')
print(getData())

gData = lambda : datetime.strftime(datetime.now(), '%d-%m-%Y')
print(gData())

print("\n")
# =======================================

st = lambda x, y: x ** y
print(st(2, 5))

print("\n")
# =======================================

def getSumm(x, y):
    return x + y

def getMultiple(x, y):
    return x * y

sumMult = lambda x, y: getSumm(x, y) - getMultiple(x, y)
print(sumMult(5, 3))




