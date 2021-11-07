from tkinter import *
from time import sleep

def pressSpace(event):
    for i in range(200):
        cnv.move(evil, 2, 0)

root = Tk()
root.geometry(f"{640}x{480}")

cnv = Canvas(root, width=640, height=480)
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)
cnv.focus_set()

evilCircle = PhotoImage(file="circle.png")            # Загружаем изображение
evil = cnv.create_image(120, 240, image=evilCircle)

cnv.bind("<space>", pressSpace)                       # Назначаем на пробел метод pressSpace

root.mainloop()