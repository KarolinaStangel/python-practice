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
    if b != 0:
        print("Brak rozwiązania.")
    elif b == 0:
        print("Istnieje nieskończenie wiele rozwiązań.")
elif b == 0:
    print("Wartość \"x\" wynosi 0.")
else:
    solution = round((-b / a), 2)
    print("Wartość \"x\" wynosi " + str(solution))
