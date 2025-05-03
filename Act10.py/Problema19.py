import re
txt = input("Introduce un texto ").split()
patron = r"^[A-Z][a-z]*[,]?$" 
lista = []
for i in txt:
    if re.match(patron, i):
        lista.append(i)
print(lista)
