# Zadanie 1
# Rozwiązać równanie ax+b=0.


def get_coefficient(coefficient_name):
    number = input("Podaj " + coefficient_name + ": ")
    while True:
        try:
            return float(number)
        except:
            number = input("Nieprawidłowa wartość. Spróbuj jeszcze raz podać współczynnik " + coefficient_name + ".\n")


def solve_linear_equation(first_coefficient, second_coefficient):
    equasion = str(a) + "x + " + str(b) + " = 0"
    if first_coefficient == 0:
        if second_coefficient == 0:
            print("Równanie " + equasion + " ma nieskończenie wiele rozwiązań.")
        else:
            print("Równanie " + equasion + " jest sprzeczne.")
    else:
        x = 0 - second_coefficient / first_coefficient
        print("Rozwiązaniem równania " + equasion + " jest:")
        print("x = " + str(round(x, 2)))


print("Będziemy rozwiązywać równanie o postaci:")
print("ax + b = 0")
print("Podaj współczynniki a i b, aby otrzymać rozwiązanie.")

a = get_coefficient("a")
b = get_coefficient("b")

solve_linear_equation(a, b)
