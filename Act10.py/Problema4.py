lista = []
with open('Estudiantes.txt', 'r') as archivo:
    for linea in archivo:
        datos = linea.split(",")
        dic = {
            "nombre": datos[0],
            "edad": int(datos[1]),
            "calificaciones": [int(i) for i in datos[2:]]
        }
        lista.append(dic)
print(lista)
