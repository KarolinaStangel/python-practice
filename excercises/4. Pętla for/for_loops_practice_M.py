fruits = ["apple", "pear", "orange", "banana"]

print("Fruits: ")
for fruit in fruits:
    print("- ", fruit + ",")
print("_______________")

print("Fruits: ")
size = len(fruits)
for i in range(size):
    print(str(i + 1) + ".", fruits[i])
print("_______________")

print("Fruits: ")
size = len(fruits)
i = 0
while i < size:
    print(str(i + 1) + ".", fruits[i])
    i += 1
