nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
def nombre_edad(nombre, edad):
    if edad == "":
        print("Hola " + nombre + ", tienes 18 años")
    else:
         print("Hola " + nombre + ", tienes " + str(edad) + " años")

nombre_edad(nombre, edad)
