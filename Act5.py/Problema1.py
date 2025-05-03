n = int(input("Ingresa el número de filas "))
m = int(input("Ingresa el número de columnas "))
for i in range(n):
    fila = []
    for j in range(m):
        if (i + j) % 2 == 0:
            fila.append(0)
        else:
            fila.append(1)
    print(fila)