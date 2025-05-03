cant_compras = int(input("¿Cuántos articulos diferentes compraste? "))
lista = []
for i in range(cant_compras):
    datos = input("Ingresa la cantidad de articulos, el nombre y el precio pagado por ellos ").split()
    cantidad = int(datos[0])
    nombre = str(datos[1])
    precio = float(datos[2])
    precio_unitario = precio / cantidad
    total = (nombre, cantidad, precio)
    lista.append(total)
suma = 0
for i in range(len(lista)):
    suma += lista[i][2]
print("El total gastado es: ", suma)