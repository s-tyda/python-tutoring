# Napisz własny program, który odczytuje a i n i zwraca a do potęgi n.
a = int(input())
n = int(input())
wynik = 1
for i in range(n):
    wynik = wynik*a
print(wynik)