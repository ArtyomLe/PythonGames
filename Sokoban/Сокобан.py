from tkinter import *

root = Tk()
root["bg"] = "#2F3F4F"                                   # Цвет фона
root.geometry("480x360")                                 # Размер основного окна

cnv = Canvas(root, width=240, height=180, bg="#AAAAAA")  # Создаём виджет Canvas с размерами width & height
cnv.config(highlightthickness=0)                         # Убираем белую рамку вокруг окна Canvas
cnv.place(x=50, y=50)                                    # Устанавливаем в область основного окна с отступом x, y


root.mainloop()