#Napisz program, który wyznacza sumę cyfr zadanej liczby całkowitej.
a = int(input())
wynik = 0
while a > 0:
    wynik = wynik + a % 10
    a = a // 10
print(wynik)