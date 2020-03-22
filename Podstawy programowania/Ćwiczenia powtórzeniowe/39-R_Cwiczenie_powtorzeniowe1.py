# Zadanie 1
# Rozwiązać równanie ax+b=0.

def get_number(name):
    num = input("Podaj liczbę " + name + ": ")
    while True:
      try:
          num = float(num)
          break
      except:
          num = input("Błąd, podaj liczbę: ")
    return num

def get_decision():
    choice = input("Czy chcesz policzyć jeszcze raz? (t/n) ")
    while True:
        if choice == "t":
            return choice
        elif choice == "n":
            print("\nDziękuję za skorzystanie z mojego programu.\n")
            return choice
        choice = input("Błędny wybór! Wybierz 't' lub 'n': ")

def prevent_0_div():
    a = get_number("a")
    while True:
        if a != 0:
            return a
        else:
            print("Nie dzieli się przez 0.")
            a = get_number("a")

choice = "t"
while choice == "t":
    print("Mamy równanie: ax+b=0. \nW celu obliczenia warości x proszę wprowadzić wartości dla zmiennych a i b:")
    a = prevent_0_div()
    b = get_number("b")
    x = (-b)/a
    print("x =", round(x, 2))
    choice = get_decision()

