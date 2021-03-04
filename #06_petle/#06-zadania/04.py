#Napisz program, który wczyta ze standardowego wejścia dwie liczby całkowite n i m,
# a następnie wyświetli wszystkie całkowite z przedziału domkniętego [n, m].

n = int(input())
m = int(input())
for i in range(n, m+1):
    print(i)
