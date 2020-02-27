import random

names = ["Ania", "Kasia", "Gosia"]
print(names)

print("-----")

for name in names:
    print(name)

print("-----")

size = len(names)           # is equal to 3
for i in range(size):
    print(str(i + 1) + ". " + names[i])

print("-----")

i = 0
length = len(names)         # is equal to 3
while i < length:
    print(names[i])
    i += 1  # i++

print("-----")

random_number = 0
while random_number != 10:
    random_number = random.randint(0, 20)
    print(random_number)
