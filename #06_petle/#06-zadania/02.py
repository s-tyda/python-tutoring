# Napisz program, w którym wczytujemy 5 liczb wprowadzonych przez użytkownika do tablicy.
# Następnie wszystkie liczby należy podnieść do kwadratu i wyświetlić.

lista = []
for _ in range(5):
    x = int(input())
    lista.append(x)

for i in lista:
    print(i ** 2)
