lista1 = str(input("Ingresa una lista de números : ")).split()
lista = [int(i) for i in lista1]
print("la lista sin elementos repetidos es :", set(lista1))
