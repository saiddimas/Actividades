
matriz1 = []
for i in range(3):
    fila = input(f"Fila {i+1} de la matriz 1: ").split()
    fila = [int(num) for num in fila]  
    matriz1.append(fila)
matriz2 = []
for i in range(3):
    fila = input(f"Fila {i + 1} de la matriz 2: ").split()
    fila = [int(num) for num in fila]  
    matriz2.append(fila)
matriz3 = []
for i in range(3):
    suma = []
    for j in range(3):
        suma.append(matriz1[i][j] + matriz2[i][j])
    matriz3.append(suma)

print("La matriz resultante es:", matriz3)