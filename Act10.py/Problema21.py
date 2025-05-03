import re
codigo = input("Ingresa el código postal ")
patron = "^([0-9]{5})|([0-9]{5}\-[0-9]{5})$"
if re.match(patron, codigo):
    print("Código postal válido")
else:
    print("Código inválido")