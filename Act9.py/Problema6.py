num = int(input("Ingresa la poscisión n-ésima: "))
lista = [0, 1]
def secuencia(num):

    if num < len(lista):
        
        return lista[num]
    else: 
        lista.append(secuencia(num - 1) + secuencia (num - 2))
        return lista[num]
print("El número de Fibonacci en la posición", num, "es", secuencia(num))
