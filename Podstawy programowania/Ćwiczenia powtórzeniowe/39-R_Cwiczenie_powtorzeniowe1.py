# Zadanie 1
# Rozwiązać równanie ax+b=0.

def num_choice(name):
    while True:
      num = input("Podaj liczbę "+name+": ")
      try:
          num = float(num)
          break
      except:
          num = input("Błąd, podaj liczbę: ")
    return num

def decision():
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
    print("Mamy równanie: ax+b=0. \nW celu obliczenia warości x proszę wprowadzić wartości dla zmiennych a i b:")
    a = num_choice("a")
    b = num_choice("b")
    x = (-b)/a
    print("x =", round(x, 2))
    choice = decision()

