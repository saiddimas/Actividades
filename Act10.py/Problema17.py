import re 
fecha  = input("Ingresa la fecha (Forma DD/MM/AAAA) ")
patron = "(0[1-9]|[12][0-9]|[3][0-1])\/(0[1-9]|1[0-2])\/[0-9]{4}$"
if re.match(patron, fecha):
    print("Fecha valida")
else:
    print("Fecha invalida")