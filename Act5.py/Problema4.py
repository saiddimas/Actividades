fila1 = input("Ingrese la primera fila de la matriz: ").split()
fila2 = input("Ingrese la segunda fila de la matriz: ").split()
fila3 = input("Ingrese la tercera fila de la matriz: ").split()
matriz = [fila1, fila2, fila3]

def transpuesta(matriz):
    matrizT = []
    for i in range(0, 3):
        matriz2 = [matriz[0][i], matriz[1][i], matriz[2][i]]
        matrizT.append(matriz2)
    return matrizT
print("La matriz transpuesta es:", transpuesta(matriz)) 