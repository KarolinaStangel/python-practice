# Zadanie 2
# Rozwiązać równanie ax2+bx+c=0.

import math


def get_coefficient(coefficient_name):
    number = input("Podaj " + coefficient_name + ": ")
    while True:
        try:
            return float(number)
        except:
            number = input("Nieprawidłowa wartość. Spróbuj jeszcze raz podać współczynnik " + coefficient_name + ".\n")


def get_delta(a, b, c):
    return b * b - 4 * a * c


print("Będziemy rozwiązywać równanie o postaci:")
print("ax^2 + bx + c = 0")
print("Podaj współczynniki a, b i c, aby otrzymać rozwiązanie.")

a: float = get_coefficient("a")
b: float = get_coefficient("b")
c: float = get_coefficient("c")

equasion: str = str(a) + "x^2 + " + str(b) + "x + " + str(c) + " = 0"
delta: float = get_delta(a, b, c)

if a == 0:
    print("Równanie " + equasion + " nie jest równanim kwadratowym.")
elif delta < 0:
    print("Równanie " + equasion + " nie ma rozwiązań w zbiorze liczb rzeczywistych.")
elif delta == 0:
    x = (0 - b) / (2 * a)
    print("Rozwiązaniem równania " + equasion + " jest x = " + str(x) + ".")
else:
    x1 = (0 - b - math.sqrt(delta)) / (2 * a)
    x2 = (0 - b + math.sqrt(delta)) / (2 * a)
    print("Rozwiązaniem równania " + str(a) + "x + " + str(b) + " = 0 są liczby: ")
    print("x1 = " + str(round(x1, 2)))
    print("x2 = " + str(round(x2, 2)))
