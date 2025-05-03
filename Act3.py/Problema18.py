def calcular_mediana(lista):
    # Ordenamos con función la lista recibida
    lista_ordenada = sorted(lista)
    # n es la cantidad de elementos de la lista
    n = len(lista_ordenada)
    if n % 2 == 0:  # Si n es par
        # Calculamos la posición de los elementos centrales
        n1 = lista_ordenada[n // 2]
        n2 = lista_ordenada[n // 2 -1]
        mediana = (n1 + n2) / 2
    else:
        mediana = lista_ordenada[n // 2]
    return mediana

numeros = [4, 2, 9, 1, 5, 6]
resultado = calcular_mediana(numeros)
print("La mediana es:", resultado)
