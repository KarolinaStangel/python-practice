user_choice = input("Wpisz liczbę od 1 do 6: \n")
while True:
    if user_choice.isdigit():
        user_choice = int(user_choice)
        if user_choice in range(1, 7):
            break
    user_choice = input("Zła wartość. Wpisz liczbę 1-7.\n")

