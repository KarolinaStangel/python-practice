# Pobierz od użytkownika 3 liczby całkowite i oblicz ich średnią.

num1 = int(input("Wpisz jakąś liczbę całkowitą:\n"))
num2 = int(input("...i następną:\n"))
num3 = int(input("...i jeszcze jedną:\n"))

sum = num1 + num2 + num3
res = sum / 3
print("Suma podanych przez Ciebie liczb wynosi: " + str(sum) + ", a ich średnia wynosi " + str(res))



