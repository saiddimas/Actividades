accion = input("¿Qué deseas hacer? ").strip().lower()
agenda = {"juan": "2384"}
if accion == "buscar":
    nombre = input("Escribe el nombre de la persona que deseas buscar: ").strip().lower()
    print("El número de ", nombre, " es: ", agenda[nombre])
elif accion == "agregar":
    nombre1 = input("Escribe el nombre de la persona que deseas agregar: ").strip().lower()
    numero1 = input("Escribe el número de la persona que deseas agregar: ").strip().lower()
    agenda[nombre1] = numero1
    print("El número ", numero1, " de ", nombre1, " ha sido agregado a la agenda.")
else:
    nombre2 = input("Escribe el nombre de la persona que deseas eliminar: ").strip().lower()
    if nombre2 not in agenda:
        print("La persona ", nombre2, " no se encuentra en la agenda.")
    else:
        del agenda[nombre2]
        print(nombre2, " ha sido eliminado de la agenda.")