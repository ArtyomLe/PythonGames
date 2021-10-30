"""
import winsound
winsound.Beep(261, 300) # До
winsound.Beep(277, 300) # Ре
winsound.Beep(293, 300) # Ми
winsound.Beep(311, 300) # Фа
winsound.Beep(329, 300) # Соль
"""

from winsound import Beep
from time import sleep

freq = [440, 330, 440, 330, 440, 415, 415, 415, 330, 415, 330, 415, 440, 440]     # Числа обязательно должны быть целыми
duration = [330, 330, 330, 330, 330, 330, 330, 330, 330, 330, 330, 330, 330, 330] # Числа обязательно должны быть целыми
pause = [0, 0, 0, 0, 0, 0, 0.5, 0, 0, 0, 0, 0, 0, 0]                              # Необязательно должны быть целыми
for i in range(len(freq)):
    try:
        Beep(freq[i], duration[i])
        sleep(pause[i])
    except:
        print("Невозможно проиграть ноту!")


