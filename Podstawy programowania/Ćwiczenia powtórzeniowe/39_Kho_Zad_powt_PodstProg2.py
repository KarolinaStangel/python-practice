import math
import cmath


# 1
def get_number(text):
    number = input(text)
    while True:
        try:
            number = float(number)
            break
        except:
            number = input("Błędna wartość. Spróbuj ponownie:\n")
    return number


print("Mamy dane równanie ax + b = 0")
a = get_number("Podaj a:\n")
b = get_number("Podaj b:\n")
if a == 0:
    print("Brak rozwiązania.")
elif b == 0:
    print("Wartość \"x\" wynosi 0.")
else:
    rozw = (-b / a)
    print("x = " + str(rozw))


# 2
def get_number(text):
    number = input(text)
    while True:
        try:
            number = float(number)
            break
        except:
            number = input("Błędna wartość. Spróbuj ponownie:\n")
    return number


print("Mamy dane równanie kwadratowe ax^2+bx+c=0.")
a = get_number("Podaj a:\n")
b = get_number("Podaj b:\n")
c = get_number("Podaj c:\n")

delta = (b**2) - (4*a*c)

if a == 0:
    print("To nie jest równanie kradratowe.")
elif delta > 0:
    print("Delta wynosi " + str(delta))
    rozw_1 = round((-b-math.sqrt(delta))/(2*a), 2)
    rozw_2 = round((-b+math.sqrt(delta))/(2*a), 2)
    print("Rozwiązania tego równania kwadratowego: x\u2081 = " + str(rozw_1) + ", " + "x\u2082 = " + str(rozw_2) + ".")
else:
    print("Równanie nie ma rozwiązania w zbiorze liczb rzeczywistych.")


#3
def triangle_sides():
    a = get_side("Podaj długość pierwszego boku trójkąta (a):\n")
    b = get_side("Podaj długość drugiego boku trójkąta (b):\n")
    c = get_side("Podaj długość trzeciego boku trójkąta (c):\n")
    return a, b, c


def get_side(text):
    number = input(text)
    while True:
        try:
            number = float(number)
            break
        except:
            number = input("Błędna wartość. Spróbuj ponownie:\n")
    return number


(a, b, c) = triangle_sides()
while True:
    if (a + b < c) or (b + c < a) or (c + a < b):
        print("Z podanych długości boków nie powstanie trójkąt. Spróbuj ponownie.")
    else:
        p = (a + b + c) / 2
        triangle_area = P = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
        print("Pole trójkąta o podanych długościach boków wynosi " + str(triangle_area) + ".\n")
        break
    (a, b, c) = triangle_sides()
