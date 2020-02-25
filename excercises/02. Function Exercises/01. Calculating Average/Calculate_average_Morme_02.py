def getNumber1():
    return int(input("Podaj pierwszą liczbę: "))

def getNumber2():
    return int(input("Podaj drugą liczbę: "))

def getNumber3():
    return int(input("Podaj trzecią liczbę: "))

def calculateAverage():
    average = (getNumber1() + getNumber2() + getNumber3()) / 3
    return round(average, 2)

print("Podawaj tylko liczby całkowite")

print(calculateAverage())
