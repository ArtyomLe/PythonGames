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

# Кнопка посмотреть собранное
seeButton = Button(root, text="Посмотреть, как должно быть", width = 56)
seeButton.place(x=10, y=620)
# seeButton.bind("<Button-1>", seeStart)
# seeButton.bind("<ButtonRelease>", seeEnd)



root.mainloop()