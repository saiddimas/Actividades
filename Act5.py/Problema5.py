fila1 = input("Ingrese la primera fila de la matriz: ").split()
fila2 = input("Ingrese la segunda fila de la matriz: ").split()
fila3 = input("Ingrese la tercera fila de la matriz: ").split()
matriz = [fila1, fila2, fila3]
elemento = input("Ingrese el elemento a buscar: ")
def busqueda(matriz, elemento):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == elemento:
                print("El elemento se encuentra en la matriz en la fila " + str(i) + " y columna " +  str(j))
  
                return i, j
busqueda(matriz, elemento)