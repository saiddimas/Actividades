accion = input("¿Qué acción deseas realizar? (Buscar o agregar) ").strip().lower()
productos = {"libro": "28.50"}
if accion == "buscar":
    nombre = input("Ingresa el nombre del producto: ").strip().lower()
    if nombre in productos:
        print(f"El producto {nombre} tiene un precio de {productos[nombre]}")
    else:
        print("El producto no se encuentra en catálago.")
elif accion == "agregar":
    nombre = input("Ingresa el nombre del producto: ").strip().lower()
    precio = float(input("Ingresa el precio del producto: "))
    productos[nombre] = precio
    print("El producto ", nombre, "ha sido agregado con exito por un precio de ", {productos[nombre]})