import time
#Zadanie 1:
#Wydrukuj liczby od 0 do 20 (linia po linii)
"""
numbers = []
for x in range(0, 21):
    numbers.append(x)
for numb in numbers:
    print(numbers[numb])
print("-----------------")

time.sleep(1)

for x in range(8):
    print(x)
print("-----------------")

for x in range(4, 9):
    print(x)
print("-----------------")

for x in range (10, 20, 3):
    print(x)
print("-----------------")

#Zadanie 2:
#Wydrukuj liczby od 1 do 10.

for x in range(1, 11):
    print(x)

#Zadanie 3:
#Wydrukuj liczby od 5 do 10 i od 50 do 55.
#Istnieje wiele możliwych rozwiązań.

for x in range(5, 11):
    print(x)
for x in range(50, 56):
    print(x)


#Zadanie 4:
#Wydrukuj tylko liczby podzielne przez 4 w przedziale od zera do 100.

for x in range(0, 101):
    if x%4 == 0:
        print(x)
        


#Zadanie 5:
#Wydrukuj liczby od 9 do 18 bez liczby 13.

for x in range(9, 13):
    print(x)
for x in range(14, 19):
    print(x)
    


#Zadanie 6:
#Wydrukuj liczby od 0 do 100 bez liczb podzielnych przez 7.

for x in range(0, 101):
    isdivisible = x % 7 == 0
    if isdivisible != True:
        print(x)

"""
#Zadanie 7:
#Print all numbers from 0 to 5, and print a message when the loop has ended.

for x in range(0, 6):
    print(x)
print("KONIEC")
print("-----------------------")

#Zadanie 8:
#Wydrukuj liczby od 20 do 0 (w kolejności malejącej).

numbers = []
for x in range(-1, 21):
    numbers.append(x)
print(numbers[21:0:-1])

print("-----------------------")

#Zadanie 9:
#Spróbuj zgadnąć, co wydrukuje program. Zapisz odpowiedź w zmiennej "your_answer_is".
#Następnie puść program i zobacz, czy zgadłeś.

items = ['cat', 'dog', 'deer']

while items:
    print(items, end="-")
    items.pop()

your_answer_is="\nWydrukuje się: ['cat', 'dog', 'deer']" #write your answer here

print(your_answer_is)
time.sleep(5)
print("\nMy answer is wrong.")
