lista = []
with open('DatosEmpleados', 'r') as archivo:
    for linea in archivo:
        info_empleados = linea.split(",")
        info = {"nombre": info_empleados[0],
                "edad": int(info_empleados[1]),
                "salario": float(info_empleados[2])
                }
                
        lista.append(info)
suma = 0
cant = len(lista)
for i in lista:
    suma += i["salario"]
promedio = suma / cant
print(promedio)
