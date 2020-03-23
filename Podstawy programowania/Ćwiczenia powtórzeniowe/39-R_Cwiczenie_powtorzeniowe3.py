# Zadanie 3
# Wczytać długości 3 boków trójkąta. Sprawdzić czy z podanych trzech długości odcinków
# można zbudować trójkąt, jeżeli tak obliczyć jego pole.
# P=sqrt(p*(p-a)*(p-b)*(p-c)),
# gdzie p jest połową obwodu.
import math

def get_number(name):
    number = input("Podaj liczbę " + name + ": ")
    while True:
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
        choice = input("Błędny wybór! Wybierz 't' lub 'n': ")

choice = "t"
while choice == "t":



    choice = get_decision()
