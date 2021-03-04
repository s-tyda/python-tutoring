# Napisać program, który wyświetli liczby podzielne przez 3 z przedziału od 1 do 100.

for i in range(1, 100):
    if i % 3 == 0:
        print(i)
