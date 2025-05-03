import re
correo = input("Ingresa tu correo: ")
patron = ".*\@.*\.[a-zA-Z]{3}"
if re.match(patron, correo):
    print("Dirreción de correo valida")
else:
    print("Dirección de correo invalida")