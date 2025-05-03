lista1 = input("Ingresa una lista de números ")
lista1 = lista1.split()
lista = []
for i in lista1:
    lista.append(int(i))
def pares(lista):
    nueva_lista = []
    for i in lista:
        if i % 2 == 0:
            nueva_lista.append(i)
    return nueva_lista
print("La lista de números pares es: ", pares(lista))