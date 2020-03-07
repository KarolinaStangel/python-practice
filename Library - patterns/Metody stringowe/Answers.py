# 1. Utwórz zmienną quote i przypisz jej następującą wartość:   'A good programmer is someone who always looks both ways before crossing a one-way street'

quote = 'A good programmer is someone who always looks both ways before crossing a one-way street'

# 2. Wyświetl tekst napisany tylko wielkimi literami

quote.upper()
# lub
print(quote.upper())

# 3. Wyświetl tekst zapisany tylko małymi literami

quote.lower()
# lub
print(quote.lower())

# 4. Sprawdź czy tekst kończy się słowem 'street'

quote.endswith('street')
# lub
print(quote.endswith('street'))


# 5. Sprawdź czy tekst jest zapisany wielkimi literami

quote.isupper()
# lub
print(quote.isupper())

# 6. Sprawdź, czy tekst skonwertowany do wielkich liter jest zapisany wielkimi literami (Zastosuj złożenie funkcji)

quote.upper().isupper()
# lub
print(quote.upper().isupper())


# 7. Poszukaj na której pozycji (licząc od zera) znajduje się w tekście słowo 'one'

quote.find('one')
# lub
print(quote.find('one'))


# 8. Zamień w tekście słowo 'one' na '1'

quote.replace('one', '1')
# lub
print(quote.replace('one','1'))


# 9. Zamień w tekście słowo 'one' na '1' a słowo 'both' na 2

quote.replace('one', '1').replace('both','2')
# lub
print(quote.replace('one','1').replace('both','2'))


# 10. Rozdziel napis na mniejsze napisy ze względu na znak rozdzielający jakim jest spacja

quote.split(' ')
# lub
print(quote.split(' '))

# 11. Sprawdź czy napis jest liczbą, liczbą dziesiętną, napisem bez cyfr, napisem z literami i cyframi
# W tym zadaniu otrzymujesz 4 wartości false. Zwłaszcza 2 ostatnie wyniki mogą Cię dziwić. Nasz napis zawierał spacje,
# składał się z wielu wyrazów i dlatego nie jest alfa-stringiem ani alfanumerykiem

quote.isdigit()
quote.isdecimal()
quote.isalpha()
quote.isalnum()
# lub
print(quote.isdigit())
print(quote.isdecimal())
print(quote.isalpha())
print(quote.isalnum())
