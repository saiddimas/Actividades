import re
txt = input("Ingresa un texto: ").split()
patron = r"^-?\d+\.\d+$"
lista = []
for i in txt:
    if re.match(patron, i):
        lista.append(i)
print(lista)
   