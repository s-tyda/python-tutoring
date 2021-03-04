# Napisać program, który będzie wczytywał od użytkownika liczby całkowite.
# Jeśli zostanie wprowadzona liczba zero, program ma wyświetlić sumę wprowadzonych liczb i się zakończyć.

x = int(input())
suma = x
while x != 0:
    x = int(input())
    suma += x
print(suma)
