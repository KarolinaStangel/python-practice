for x in range(8):
    print(x)

for x in range(4, 9):
    print(x)

for x in range (10, 20, 3):
    print(x)

#1
for s in range(0, 21):
    print(s)

print("----------------")

#2
for s in range(1, 11):
    print(s)
print("----------------")

#3
for s in range(5, 56):
    if s not in range(11, 50):
        print(s)
print("----------------")

#4
for s in range(1, 101):
    if s % 4 == 0:
        print(s)
print("----------------")

#5.1
for s in range(9, 19):
    if s != 13:
        print(s)
print("----------------")

#5.2
for s in range(9, 19):
    if s == 13:
        continue
    print(s)
print("----------------")

#6
for s in range(0, 101):
    if s % 7 != 0:
        print(s)
print("----------------")

#7
for s in range(0, 6):
    print(s)
print("The loop has ended.")
print("----------------")

#8.1
for s in reversed(range(0, 21)):
    print(s)
print("----------------")

#8.2
for s in range(20, -1, -1):
    print(s)
print("----------------")

#9
items = ['cat', 'dog', 'deer']

while items:
    print(items, end="-")
    items.pop()

your_answer_is=""
print(your_answer_is)



