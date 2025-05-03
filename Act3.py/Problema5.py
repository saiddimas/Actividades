calificaciones = input("Ingresa la lista de calificaciones: ")
numlista = []
lista = calificaciones.split()
for calificaciones in lista:
    numlista.append(int(calificaciones))
def promedio(numlista):
    suma = sum(numlista)
    div = len(numlista)
    promedio = suma/div
    return promedio
print(promedio(numlista))