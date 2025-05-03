lista11 = input("Ingresa una lista de números : ").split()
lista22 = input("Ingresa otra lista de números : ").split()
lista1 = [int(i) for i in lista11]
lista2 = [int(i) for i in lista22]
conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = conjunto1 & conjunto2
print("El conjunto de la intersección es :", conjunto3)