# Napisz program, który wczytuje n liczb, a następnie wyświetla je w odwrotnej kolejności.

a = input().split()
a = a[::-1]
for i in a:
    print(i, end=" ")
