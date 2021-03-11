# Napisz program, który stwierdza czy liczba jest pierwsza.

suma = 0
a = int(input())
for i in range(2, a):
    if a % i != 0:
        suma += 1
if suma == a - 2:
    print("Prawda")
else:
    print("Fałsz")