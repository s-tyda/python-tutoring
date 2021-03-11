# Napisz program, który obliczy liczbę dzielników podanej liczby.

suma = 0
a = int(input())
for i in range(1, a + 1):
    if a % i == 0:
        suma += 1
print(suma)