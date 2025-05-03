lista1 = str(input("Ingresa una lista de números : ")).split()
lista = [int(i) for i in lista1]
conjunto = set(lista)
if not conjunto :
    print("La lista está vacía ")
else:
    print("La lista no está vacía")