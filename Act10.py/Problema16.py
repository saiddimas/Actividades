import re
numero = input("Ingresa el número de celular ")
patron = "^\+[0-9]{2}\-[0-9]{4}\-[0-9]{4}$" 
if re.match(patron, numero):
    print("Numero de celular valido")
else: 
    print("Numero invalido")