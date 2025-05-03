fila11 = input("Ingrese la primera fila de la matriz: ").split()
fila22 = input("Ingrese la segunda fila de la matriz: ").split()
fila33 = input("Ingrese la tercera fila de la matriz: ").split()
fila44 = input("Ingrese la cuarta fila de la matriz: ").split()
fila55 = input("Ingrese la quinta fila de la matriz: ").split()
fila1 = [int(i) for i in fila11]
fila2 = [int(i) for i in fila22]    
fila3 = [int(i) for i in fila33]
fila4 = [int(i) for i in fila44]
fila5 = [int(i) for i in fila55]
matriz = [fila1, fila2, fila3, fila4, fila5]
principal = 0
secundaria = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
       
        if i == j:
            principal += matriz[i][j]
        if i +  j == len(matriz) - 1:
            secundaria += matriz[i][j]
suma = principal + secundaria
print("La suma de los elementos de la diagonal principal es:", principal, ", de la secundaria es " , secundaria, ", y su suma es", suma)