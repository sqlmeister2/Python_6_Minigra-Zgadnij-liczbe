#import funkcji randint
from random import randint

#sprawdzenie sto razy funkcji losującej od 1 do 10
# for i in range(100):
#    print(randint(1,10))

los = randint(1,10)
odp = -1
licznik = 0
print("Zgadnij liczbę z przedziału od 1 do 10")

while odp != los:
    licznik += 1
    odp = int(input("Wpisz liczbe\n")) #przekonwertowanie typu na liczbowy
    if odp > los:
        print("Wylosowana liczba jest mniejsza niż odpowiedź")
    elif odp < los:
        print("Wylosowana liczba jest większa niż odpowiedź")
    else:
        print("Zgadłes liczbe za", licznik,"razem")

