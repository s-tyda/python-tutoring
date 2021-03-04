# pętla for - konkretna ilość razy (n), kiedy nie interesuje nas wartość elementu
n = int(input())
for _ in range(n):
    print("coś")

# pętla for - konkretna ilość razy (n), ale interesuje nas wartość elementu
for i in range(n):
    print(i)

# pętla for - dla każdego elementu listy lub innego obiektu
lista = [1, 5, 19]
for i in lista:
    print(i)

napis = "Dominik"
for i in napis:
    print(i)

# pętla for z enumerate() - kiedy interesuje nasz indeks oraz element jednocześnie
for index, element in enumerate(lista):
    print(element, index)

# while - dopóki warunek jest spełniony
while n < 6:
    n = n + 1
print(n)
