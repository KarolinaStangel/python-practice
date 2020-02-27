# Pobierz od użytkownika 3 liczby całkowite i oblicz ich średnią.

def get_num():
    return int(input("Wpisz jakąś liczbę całkowitą:\n"))


num1 = get_num()
num2 = int(input("...i następną:\n"))
num3 = int(input("...i jeszcze jedną:\n"))

list = []
list.append(num1)
list.append(num2)
list.append(num3)

sum = 0
for x in list:
    sum += x

size = len(list)
res = sum / size

print("Suma podanych przez Ciebie liczb wynosi: " + str(sum) + ", a ich średnia wynosi " + str(res))



