cant_empleados = int(input("Ingresa la cantidad de empleados: ")) 
empleados = []
for i in range(cant_empleados):
    nombre = input("Ingresa el nombre del empleado: ")
    edad = int(input("Ingresa la edad del empleado: "))
    salario = float(input("Ingresa el salario del empleado: "))
    info_empleados = {
        "nombre": nombre,
        "edad": edad,
        "salario": salario,
    }
    empleados.append(info_empleados)
#empleados = [str(i) for i in empleados]

with open('DatosEmpleados', 'w') as archivo:
    for empleado in empleados:
        archivo.write(f"{empleado['nombre']},{empleado['edad']},{empleado['salario']}\n")
        