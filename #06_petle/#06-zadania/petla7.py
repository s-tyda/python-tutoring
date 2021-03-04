#Napisz program, który wczyta tekst od użytkownika i wyświetli co drugi znak.
a = input()
b = a[::2]
for i in b:
    print(i)