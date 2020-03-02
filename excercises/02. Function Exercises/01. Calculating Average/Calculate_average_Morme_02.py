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

numbers = []

def getNumber():
    return (input("Podaj liczbę: "))

i = 0
sum = 0
while i < 5:
    numbers.append(getNumber())
    sum += int(numbers[i])
    i += 1

size = len(numbers)
average = sum / size

print(round(average, 2))
