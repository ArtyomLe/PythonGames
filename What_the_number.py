# Угадай число

import random                   # Включаем библиотеку генерации случайных чисел

lowDigit  = 10                  # Нижняя граница случайного числа
highDigit = 50                  # Верхняя граница случайного числа
digit     = 0                   # Загаданное компьютером число

win        = False              # Угадал текущее число?
playGame   = True               # Продолжается ли игра?
x          = 0                  # Число, которое вводит пользователь

countInput = 0                  # Количество попыток угадать
startScore = 100                # Начальное кол-во очков
score      = 0                  # Текущее кол-во очков
maxScore   = 0                  # Максимальное кол-во очков за сессию игры

# =====================================================

while(playGame):                              # Основной цикл (mainloop)
    digit = random.randint(lowDigit, highDigit)
    countInput = 0
    score = startScore
    print("Компьютер загадал число, попробуйте отгадать!")
#   print(f"Загаданное число: {digit}")

    
    while(not win and score > 0):             # Внутрений цикл отвечает за один раунд
        print("-" * 30)
        print(f"Заработано очков: {score}")
        print(f"Рекорд: {maxScore}")
        
        x = ""                                # Сбрасываем для условия While
        while(not x.isdigit()):               # Контроль чтобы пользователь ввёл обязательно число
            x = input(f"Введите число в диапазоне от {lowDigit} до {highDigit}: ")
            if(not x.isdigit()):
                print("." * 40 + " Введите, пожалуйста, число.")

        x = int(x)

        if (x == digit):
            win = True           
            
        else:
            length = abs(x - digit)
            if(length < 3):
                print("Очень горячо!(радиус 3)")
            elif(length < 5):
                print("Горячо!(радиус 5)")
            elif(length < 10):
                print("Тепло(радиус 10)")
            elif(length < 15):
                print("Прохладно(радиус 15)")
            elif(length < 20):
                print("Холодно(радиус 20)")
            else:
                print("Ледяной ветер")
                

            if(countInput == 7):
                score -= 10                 # Стоимость подсказки
                if(digit % 2 == 0):
                    print("Число чётное")
                else:
                    print("Число нечётное")
            elif(countInput == 6):
                score -= 8
                if(digit % 3 == 0):
                    print("Число делится на 3")
                else:
                    print("Число не делится на 3")
            elif(countInput == 5):
                score -= 4
                if(digit % 4 == 0):
                    print("Число делится на 4")
                else:
                    print("Число не делится на 4")
            elif(countInput > 2 and countInput < 5):
                score -= 2
                if(x > digit):
                    print("Загаданное число меньше вашего")
                else:
                    print("Загаданное число больше вашего")

            if(random.randint(0, 100) < 5): # Сбрасываем загаданое число(с вероятностью в 5%)
                print("Ой всё! Я перезагадал число!")
                digit = random.randint(lowDigit, highDigit)
#               print(f"Загаданное число: {digit}")
                
            score -= 5                       # За каждый ход вычитаем 5 очков
        countInput += 1
    print("=" * 40)    
    if(x == digit):
        print("Победа, Поздравляем!")
    else:
        print("У вас закончились очки, вы проиграли :(")
        
    if(input("Enter - сыграть ещё, 0 -  выход") == "0"):
        playGame = False
    else:
        win = False

    if(score > maxScore):
        maxScore = score

print("*" * 30)
print("Спасибо что сыграли со мной :)")
