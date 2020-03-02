"""def getNumber1():
    return int(input("Podaj pierwszą liczbę: "))

def getNumber2():
    return int(input("Podaj drugą liczbę: "))

def getNumber3():
    return int(input("Podaj trzecią liczbę: "))

def calculateAverage():
    average = (getNumber1() + getNumber2() + getNumber3()) / 3
    return round(average, 2)

print("Podawaj tylko liczby całkowite")

print(calculateAverage())"""

print("Instrukcja: ")
print("Po pojawieniu się prośby o podanie liczby, podaj wybraną przez siebie liczbę, a następnie wciśnij 'ENTER'")
print("Postępuj tak, aż do momentu wprowadzenia wszystkich liczb, z których chcesz wyliczyć średnią.")
print("Po kolejnym pojawieniu się prośby o wpisanie liczby, zamiast liczby wprowadź 'q' (UWAGA! tylko 'małe' q).")

numbers = []

def getNumber():
    return (input("Podaj liczbę: "))

i = 0
sum = 0
while i >= 0:
    numbers.append(getNumber())
    sum += int(numbers[i])
    i += 1
    if getNumber() == "q":
        break

size = len(numbers)
average = sum / size

print(round(average, 2))
