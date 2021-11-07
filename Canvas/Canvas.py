from tkinter import *

def plusSecond():
    global second
    second += 1
    label["text"] = f"Прошло секунд: {second}"
    root.after(1000, plusSecond)                # Вызываем через 1 секунду

root = Tk()
root.geometry(f"{320}x{240}")
label = Label(root)
label.place(x=10, y=10)

second = 0                                      # Секунды

plusSecond()
root.mainloop()