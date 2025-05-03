import re
nums = input("Ingresa los números de la tarjeta ")
patron = "^[0-9]{4}\-[0-9]{4}\-[0-9]{4}\-[0-9]{4}$"
if re.match(patron, nums):
    print("Tarjeta válida")
else:
    print("Tarjea no válida")