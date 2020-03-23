import math


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
    print("To nie jest równanie kwadratowe.")
elif delta > 0:
    print("Delta wynosi " + str(delta))
    result_1 = round((-b - math.sqrt(delta)) / (2 * a), 2)
    result_2 = round((-b + math.sqrt(delta)) / (2 * a), 2)
    print("Rozwiązania tego równania kwadratowego: x\u2081 = " + str(result_1) + ", " + "x\u2082 = " + str(result_2) + ".")
elif delta == 0:
    print("Delta wynosi " + str(delta) + "\nx\u2081 = 0, x\u2082 nie ma rozwiązania.")
else:
    print("Równanie nie ma rozwiązania w zbiorze liczb rzeczywistych.")
