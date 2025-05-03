import random


num = random.randint(0, 100000)
def adivinanza(num):
    while True:
        numUsuario = int(input("Adivina el número entre 0 y 100000: "))
        if numUsuario < num:
            print("El número es mayor")
        elif numUsuario > num:
            print("El número es menor")
        else:
            print("¡Adivinaste el número!")
adivinanza(num)