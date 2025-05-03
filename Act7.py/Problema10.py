ventas_totales = []
while True:
    
    producto = input("Ingresa el nombre del producto: ")
    mes = input("Ingresa el mes: ")
    cant_vendida = int(input("Ingresa la cantidad de ventas del producto: "))
    decision = input("¿Deseas agregar otro producto? ").lower()
    ventas = {"producto":producto, "mes": mes, "cant_vendida": cant_vendida}
    ventas_totales.append(ventas)
    if decision == 'no':
        break
print("El total de las ventas fueron :", )
for ventas in ventas_totales:
    print(ventas)