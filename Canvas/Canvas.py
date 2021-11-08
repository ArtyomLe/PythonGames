from tkinter import *
from time import sleep

def pressSpace(event):
    global countAnimation
    cnv.unbind("<space>")
    countAnimation += 1
    if (countAnimation < 20):
        cnv.move(evil, 2, 0)
        root.after(50, lambda e=event: pressSpace(e))
    else:
        countAnimation = 0
        cnv.bind("space", pressSpace)

root = Tk()
root.geometry(f"{640}x{480}")

cnv = Canvas(root, width=640, height=480)
cnv.config(highlightthickness=0)
cnv.place(x=0, y=0)
cnv.focus_set()

evilCircle = PhotoImage(file="circle.png")
evil = cnv.create_image(120, 240, image=evilCircle)

cnv.bind("<space>", pressSpace)

countAnimation = 0                                  # Кол-во рекурсий

root.mainloop()