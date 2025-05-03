nombres = []
with open('Nombres.txt', 'r') as archivo:
    lineas = archivo.readlines()

    for linea in lineas:
        nombres.append(linea.strip())
print(nombres)
