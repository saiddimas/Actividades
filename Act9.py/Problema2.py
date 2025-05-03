lista = input("Ingresa una lista de palabras: ").lower()
lista = lista.split()

def orden(lista):
    lista.sort()
    return lista
print("La lista ordenada es:", orden(lista))