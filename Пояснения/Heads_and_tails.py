
import random

#  Кол-во бросков

n = 10

for i in range(5):
    orel = 0
    reshka = 0

    for j in range(n):
        if(random.randint(0, 1) == 0):
            orel += 1
        else:
            reshka += 1

    print(f"Из {n} бросков отношение орла к решке {orel}/{reshka}")
