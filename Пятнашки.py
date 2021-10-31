from tkinter import *               # Общий Tkinter
from tkinter import ttk             # Для использования RadioButton
from tkinter import messagebox      # Для использования окон сообщений
from random import randint          # Случайные числа
from winsound import Beep           # Простейший генератор звука

# ============================= НАЧАЛО ПРОГРАММЫ ==========================================

root = Tk()
root.resizable(False, False)
root.title("Головоломка для отчаянных и прокажённых")
root.iconbitmap("icon/iconi.ico")

# ЦВЕТА
back = "#373737"   # Фон
fore = "#AFAFAF"   # Шрифт

WIDTH = 422
HEIGHT = 730
POS_X = root.winfo_screenwidth() // 2 - WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - HEIGHT // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{POS_X}+{POS_Y}")
root["bg"] = back

# Кнопка ПОСМОТРЕТЬ СОБРАННОЕ
seeButton = Button(root, text="Посмотреть, как должно быть", width = 56)
seeButton.place(x=10, y=620)
# seeButton.bind("<Button-1>", seeStart)       # При нажатии вызываем метод seeStart
# seeButton.bind("<ButtonRelease>", seeEnd)    # Когда отпускаем кнопку вызывается метод seeEnd

# Кнопка СТАРТ
startButton = Button(text="СТАРТ", width=56)
startButton.place(x=10, y=650)
# startButton["command"] = startNewRound

# Кнопка СБРОС
resetButton = Button(root, text="Сброс", width=56)
resetButton.place(x=10, y=680)
# resetButton["command"] = resetPictures

# Метка для вывода текста с кол-вом сделанных ходов и рекордом текущего уровня
textSteps = Label(root, bg=back, fg=fore)
textSteps.place(x=10, y=550)
textRecord = Label(root, bg=back, fg=fore)
textRecord.place(x=10, y=570)

# Метка сложности
Label(root, bg=back, fg=fore, text="Сложность:").place(x=267, y=550)

# Названия степеней сложности перемешивания
itemDiff = ["Только начал","Немного почитал","Знаю print()","Понял сортировку","Изучил лабиринт","Задонатил!"]

# Выпадающий список
diffCombobox = ttk.Combobox(root, width=20, values=itemDiff, state="readonly")
diffCombobox.place(x=270, y=570)
# diffCombobox.bind("<<ComboboxSelected>>", lambda e: refreshText())
diffCombobox.current(0)         # Значение по умолчанию 0 = "Только начал"

# Радиопереключатели
image = BooleanVar()            # Создаём переменную
image.set(True)                 # Устанавливаем значение
# Создаём радио-кнопку и привязываем к ней переменную image
radio01 = Radiobutton(root, text="Пятнашки", variable=image, value=True, activebackground=back, bg=back, fg=fore)
radio02 = Radiobutton(root, text="Природа", variable=image, value=False, activebackground= back, bg=back, fg=fore)
# radio01["command"] = isCheckImage
# radio02["command"] = isCheckImage
radio01.place(x=150, y=548)
radio02.place(x=150, y=568)

root.mainloop()