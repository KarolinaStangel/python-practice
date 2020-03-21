# Zadanie 1
# Rozwiązać równanie ax+b=0.
choice = "t"
while choice == "t":
    print("Mamy równanie: ax+b=0. \nW celu obliczenia warości x roszę wprowadzić wartości dla zmiennych a i b:")
    a = float(input("Podaj a:"))
    b = float(input("Podaj b:"))
    x = (-b)/a
    print("x =", round(x, 2))
    choice = input("Czy chcesz policzyć jeszcze raz? (t/n)")
    if choice == "t":
        pass
    elif choice == "n":
        print("\nDziękuję za skorzystanie z mojego programu.\n"+
              "Jeśli Ci się spodobał rozważ wsparcie,\n"+
              "wpłacając donację na konto: 0000 0000 0000 0001")
        break
    else:
        choice = input("Zła literka analfabeto! Spróbuj jeszcze raz.")
