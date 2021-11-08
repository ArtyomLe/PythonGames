from tkinter import *
def plusSecond():
    global second, timerLink
    second += 1
    label["text"] = f"Прошло секунд: {second}"
    timerLink = root.after(1000, plusSecond)   # Присваиваем переменной timerLink метод after

def startTimer():
    global timerLink
    timerLink = root.after(1000, plusSecond)

def stopTimer():
    global timerLink
    if (timerLink != None):
        root.after_cancel(timerLink)           # after_cancel прекращает вызов
        timerLink = None

root = Tk()
root.geometry(f"{320}x{240}")

label = Label(root)
label.place(x=10, y=10)

startBtn = Button(root, text="Старт")
startBtn.place(x=10, y=50)
startBtn["command"] = startTimer

stopBtn = Button(root, text="Стоп")
stopBtn.place(x=70, y=50)
stopBtn["command"] = stopTimer

second = 0
timerLink = None
plusSecond()

root.mainloop()