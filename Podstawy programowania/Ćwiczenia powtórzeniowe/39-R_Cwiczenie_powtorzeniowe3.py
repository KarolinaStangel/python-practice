# Zadanie 3
# Wczytać długości 3 boków trójkąta. Sprawdzić czy z podanych trzech długości odcinków
# można zbudować trójkąt, jeżeli tak obliczyć jego pole.
# P=sqrt(p*(p-a)*(p-b)*(p-c)),
# gdzie p jest połową obwodu.
import math

def get_side(name):
    number = input("Podaj długość boku " + name + ": ")
    while True:
      try:
          number = float(number)
          if number <= 0:
              number = input("Długość boku trójkąta nie może być mniejsza lub równa 0. \nPodaj jeszcze raz długość boku " + name + " ")
          else:
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
        choice = input("Błędny wybór! Wybierz 't' lub 'n': ")

choice = "t"
while choice == "t":
    print("Proszę podać długości boków trójkąta w celu obliczenia jego pola: ")
    a = get_side("a")
    b = get_side("b")
    c = get_side("c")
    while True:
        if a >= b + c:
            print("Bok a jest za długi aby mógł powstać trójkąt")
            a = get_side("a")
        elif b >= a + c:
            print("Bok b jest za długi aby mógł powstać trójkąt")
            b = get_side("b")
        elif c >= a + b:
            print("Bok c jest za długi aby mógł powstać trójkąt")
            c = get_side("c")
        else:
            break

    p = (a + b + c) / 2
    triangle_area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("Pole trójkąta wynosi: " + str(round(triangle_area, 2)))

    choice = get_decision()
