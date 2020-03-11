phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

telist = ["D", "'", "n", "i", "c", "!"]
for letter in telist:
    plist.remove(letter)

plist.insert(1, plist.pop())
plist.insert(2, plist.pop(3))
plist.insert(4, plist.pop())

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
