agenda = []
datos = {}
while True:
    accion = input("¿Qué deseas realizar? ").lower()
    if accion == "agregar":
        nombre = input("Ingresa el nombre de la persona: ").lower()
        numero = input("Ingresa su número de telefono: ")
        direccion = input("Ingresa su correo electronico: ")
        datos[nombre] = {"numero": numero, "direccion": direccion}
        decision = input("¿Desea continuar? ").lower()
        if decision == "no":
            print("Gracias por usar la agenda")
            break
    elif accion == "buscar":
        nombre = input("Ingresa el nombre de la persona: ").lower()
        if nombre in datos:
            print("El número de ", nombre, "es", datos[nombre]["numero"], "y su correo electronico es ", datos[nombre]["direccion"])
        else:
            print("No se encontró a ", nombre, "en la agenda")
            decision = input("¿Desea continuar? ").lower()
            if decision == "no":
                print("Gracias por usar la agenda")
                break
    elif accion == "eliminar":
        nombre = input("ingresa el nombre de la persona: ").lower()
        if nombre in datos:
            del datos[nombre]   
            print("Se ha eliminado a ", nombre, "de la agenda")    
            decision = input("¿Desea continuar? ").lower()
            if decision == "no":
                print("Gracias por usar la agenda")
                break
        else:
            print("No se encontró a ", nombre, "en la agenda")
            decision = input("¿Desea continuar? ").lower()
            if decision == "no":
                print("Gracias por usar la agenda")