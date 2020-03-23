# Zadanie 3
# Wczytać długości 3 boków trójkąta. Sprawdzić czy z podanych trzech długości odcinków
# można zbudować trójkąt, jeżeli tak obliczyć jego pole.
# P=sqrt(p*(p-a)*(p-b)*(p-c)),
# gdzie p jest połową obwodu.


import math


def get_side():
    length = input()
    while True:
        if length.isdigit():
            length = float(length)
            if length > 0:
                return length
        length = input("Nieprawidłowa wartość. Spróbuj jeszcze raz.\n")


def get_sides(sides_no):
    sides = []
    for number in range(sides_no):
        print(str(number + 1) + ". ", end="")
        sides.append(get_side())
    return sides


def get_circumference(sides):
    circumference = 0
    for side in sides:
        circumference += side
    return circumference


def can_make_triangle(sides):
    for side in sides:
        if side > get_circumference(sides) / 2:
            return False
    return True


def get_triangle_area(sides):
    p = get_circumference(sides) / 2
    area = 1
    for side in sides:
        area *= p - side
    return math.sqrt(p * area)


print("Będziemy liczyć pole trójkąta:")
print("Podaj długość trzech boków.")

sides = get_sides(3)

if can_make_triangle(sides):
    area = get_triangle_area(sides)
    print("Pole tego trójkąta wynosi " + str(round(area, 2)) + ".")
else:
    print("Z tych odcinków nie można zbudować trójkąta.")

