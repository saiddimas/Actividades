lista = []
with open('NumEnt.txt', 'r') as archivo:
    
    for linea in archivo:
        lista.append(int(linea.strip()))

suma = sum(lista)
print(suma)