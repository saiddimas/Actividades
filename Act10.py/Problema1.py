nombres = input("Ingresa la lista de nombres: ").split()
for i in range(len(nombres)):
    with open('Nombres.txt', 'a') as archivo:
        archivo.write(nombres[i] + '\n')