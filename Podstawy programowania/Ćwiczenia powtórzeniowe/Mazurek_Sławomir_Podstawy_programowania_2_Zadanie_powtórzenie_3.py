import math


def triangle_sides():
    a = get_side_length("Podaj długość pierwszego boku trójkąta (a):\n")
    b = get_side_length("Podaj długość drugiego boku trójkąta (b):\n")
    c = get_side_length("Podaj długość trzeciego boku trójkąta (c):\n")
    return a, b, c


def get_side_length(text):
    length = input(text)
    while True:
        try:
            length = float(length)
            if length > 0:
                return length
            else:
                length = input("Długość boku musi być liczbą dodatnią. Spróbuj jeszcze raz:\n")
        except:
            length = input("Błędna wartość. Spróbuj ponownie:\n")


(a, b, c) = triangle_sides()
while True:
    if (a + b < c) or (b + c < a) or (c + a < b):
        print("Z podanych długości boków nie powstanie trójkąt. Spróbuj ponownie.")
    else:
        p = (a + b + c) / 2
        triangle_area = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
        print("Pole trójkąta o podanych długościach boków wynosi " + str(triangle_area) + ".\n")
        break
    (a, b, c) = triangle_sides()
