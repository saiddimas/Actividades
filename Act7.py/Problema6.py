lista = []
for i in range(7):

    dia1 = input("Ingresa el día de la semana y su temperatura: ").split()
    dia = (dia1[0], int(dia1[1]))
    #tupla = (dia1[0], dia)
    lista.append(dia)
suma = 0
for i in range(len(lista)):
    suma += lista[i][1]
promedio = suma / 7
print("El promedio de la semana es: ", promedio)