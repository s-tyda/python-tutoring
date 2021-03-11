# Napisz program, który stwierdza czy liczba jest pierwsza.
import sympy

# Wersja z dodawaniem
suma = 0
a = int(input())
for i in range(2, a):
    if a % i != 0:
        suma += 1
print(suma == a - 2)

# Wersja z mnożeniem
wynik = 1
for i in range(2, a):
    if a % i == 0:
        wynik *= 0
    else:
        wynik *= 1
print(bool(wynik))

# Wersja z flagą
wynik = 1
for i in range(2, a):
    if a % i == 0:
        wynik = 0
print(bool(wynik))

# Wersja z flagą i łamaniem pętli
wynik = 1
for i in range(2, a):
    if a % i == 0:
        wynik = 0
        break
print(bool(wynik))

print(sympy.isprime(a))

print(all([a % i != 0 for i in range(2, a)]))
