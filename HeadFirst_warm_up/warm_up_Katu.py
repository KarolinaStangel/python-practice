# Uzupełnij poniższy kod o podane elementy, tak aby:
# Program sprawdził 5 razy czy aktualna minuta jest parzysta czy nieparzysta i wydrukował wynik.
# Niech pomiędzy każdym sprawdzeniem upłynie "randomowa" ilość sekund.
# Wynik ma zostać wyświetlony.

# Elementy do wstawienia:
# 1. time.sleep
# 2. import time
# 3. for i in range(5):
# 4. wait_time
# 5. import random
# 6. random.randint(1, 60)

from datetime import datetime
import time
import random

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

for i in range(5):
    right_this_minute = datetime.today().minute
    if right_this_minute in odds:
        print("This minute seems a little odd.")
    else:
        print("Not an odd minute.")
    wait_time = time.sleep
    wait_time(random.randint(1, 60))

#
# POMOCE:
# import time
# time.sleep(5)  <- liczba w nawiasach (w tym wypadku "5") określa ile sekund program będzie "czekał" zanim "pójdzie" dalej.
#
# import random
# random.randint(1,60) <- funkcję random znamy już doskonale, ale podaję dla przypomnienia.
#                         Losowana będzie randomowa liczba z przedziału podanego w nawiasach.
