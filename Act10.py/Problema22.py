import re
nombre = input("Ingresa el nombre de usuario ")
patron = "[a-zA-Z0-9\_]{3,16}$"
if re.match(patron, nombre):
    print("Nombre de usuario válido")
else: 
    print("Nombre de usuario inválido")