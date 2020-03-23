# Zadanie 2
# Rozwiązać równanie ax2+bx+c=0.
import math

def get_number(name):
    while True:
      number = input("Podaj liczbę " + name + ": ")
      try:
          number = float(number)
          break
      except:
          number = input("Błąd, podaj liczbę: ")
    return number

def get_decision():
    choice = input("Czy chcesz policzyć jeszcze raz? (t/n) ")
    while True:
        if choice == "t":
            return choice
        elif choice == "n":
            print("\nDziękuję za skorzystanie z mojego programu.\n")
            return choice
        choice = input("Błędny wybór! Wybierz t dla 'tak' lub n dla 'nie': ")


choice = "t"
while choice == "t":
    print("Mamy równanie kwadratowe: ax\u00b2+bx+c=0. \nW celu obliczenia warości x proszę wprowadzić wartości dla zmiennych a, b i c:")
    a = get_number("a")
    b = get_number("b")
    c = get_number("c")
    delta = float(b**2 - 4*a*c)
    print("delta =", round(delta, 2))
    if delta < 0:
        print("Ponieważ delta jest mniejsza od zera równanie nie ma rozwiązań w zbiorze liczb rzeczywistych.")
    elif delta == 0:
        x1 = float(( - b) - math.sqrt(delta)) / 2 * a
        x2 = float(( - b) + math.sqrt(delta)) / 2 * a
        print("Równanie ma jedno rozwiązanie:  \nx1 = x2 = "+str(round(x2, 2)))
    else:
        x1 = float(( - b) - math.sqrt(delta)) / 2 * a
        x2 = float(( - b) + math.sqrt(delta)) / 2 * a
        print("Równanie ma dwa rozwiązania: \nx1 = "+str(round(x1, 2)), "\nx2 = "+str(round(x2, 2)))
    choice = get_decision()
