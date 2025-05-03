num = input("Ingresa una lista de números separados por espacios: ")
lista = list(map(int, num.split()))
lista.sort()
print("Lista ordenada:", lista)