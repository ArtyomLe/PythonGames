import random               # Подключаем библиотеку

low_range = 10              # Нижняя граница чисел
high_range = 100            # Верхняя граница чисел
sign = 0                    # Знак операции
playGame = True             # Основной цикл
count = 0                   # Кол-во решённых примеров
right = 0                   # Правильные ответы
score = 0                   # Очки

print("""Компьютер состовляет пример. Введите ответ.
Для завершения работы введите STOP""")
print("*" * 32)

# ======== Main_loop ================================

while(playGame):
    print(f"Ваши очки: {score}")
    print(f"Обработано задач: {count}")
    print(f"Кол-во правильных ответов: {right}")
    print("-" * 22)

    sign = random.randint(0, 3)
    # 0 - plus
    # 1 - minus
    # 2 - multiplication
    # 3 - division

# ******** Plus ************

    if(sign == 0):
        z = random.randint(low_range, high_range)
        x = random.randint(low_range, z)

    
        y = z - x
        if(random.randint(0 ,1) == 0):
            print(f"{x} + {y} = ?")
        else:
            print(f"{y} + {x} = ?")
        
# ******** Minus ***********

    if(sign == 1):
        x = random.randint(low_range, high_range)
        y = random.randint(0, x - low_range)
    
        z = x - y
        print(f"{x} - {y} = ?")
    
# ******** Multiplication **

    if(sign == 2):
        x = random.randint(1, (high_range - low_range) // random.randint(1, high_range//5) + 1) 
        y = random.randint((low_range + x), high_range) // x     # (low_diapazon + x) что бы не было ситуаций умножения на ноль

        z = x * y
        print(f"{x} * {y} = ?")

# ******** Division ********
                       
    if(sign == 3):
        x = random.randint(1, (high_range - low_range) // random.randint(1, high_range//5) + 1) #  + 1 для того чтобы не получился 0
        y = random.randint((low_range + x), high_range) // x     # (low_diapazon + x) что бы не было ситуаций умножения на ноль
        # if(y == 0):  # low_range + x отменяет эти две строки, "y" не может равняться нулю 
        #   y = 1
                       
        x = x * y
        z = x // y
        print(f"{x} / {y} = ?")

# -------- user_answer_options ------

    user = ""
    while (not user.isdigit()               # До тех пор пока не будет введено десятичное число
           and user.upper() != "STOP"       # .upper Конвертирует прописные в заглавные
           and user.upper() != "S"
           and user.upper() != "Ы"
           and user.upper() != "ЫЕЩЗ"):
        user = input("Ваш ответ? ")
            
        if (user.upper() == "HELP"
                or user == "?"
                or user == ","
                or user.upper == "РУДЗ"):
            if (z > 9):
                print(f"Последняя цифра ответа: {z % 10}")
            else:
                print(f"Ответ состоит из одной цифры, подсказка невозможна.")
            score -= 10

        elif (user.upper() == "STOP"
                  or user.upper() == "S"
                  or user.upper() == "Ы"
                  or user.upper() == "ЫЕЩЗ"):
            playGame = False

        elif (not user.isdigit()):
            print("Введите повторно ваш ответ")
      
        else:
            count += 1
            if (int(user) == z):
                print("\nПравильно!\n")
                right += 1
                score += 10
            
            else:
                print(f"\nОтвет не правильный... Правильно: {z}")
                print(f"Вы можете ввести команду HELP или ? чтобы увидеть последнюю цифру ответа (-10 очков)\n")
                score -= 20
    
# ======= End_main_loop =============

print("*"*42)
print("Статистика игры: ")
print(f"Всего примеров: {count}")
print(f"Правильных ответов: {right}")
print(f"Неправильных ответов: {count - right}")

# count обязательно проверяем потому что он выступает в роли делителя и не должен быть равен нулю
if (count > 0):
    print(f"Процент верных ответов: {int(right / count * 100)}%")
else:
    print("Процент верных ответов: 0%")
print("До скорых встреч!")


           
            
