# Napisać program, który wyświetli co czwartą liczbę dwucyfrową.

for i in range(10, 100, 4):
    print(i)

x = 10
while x < 100:
    print(x)
    x += 4

for i in range(10, 100):
    if (i - 2) % 4 == 0:
        print(i)