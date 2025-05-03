import re
fecha = input("Ingresa la fecha: ")
patron = "^([0-9]{4})\-(0[1-9]|1[0-2])\-(0[1-9]|[12][0-9]|3[0-1])$"
if re.match(patron, fecha):
    print("Fecha válida")
else:
    print("Fecha inválida")