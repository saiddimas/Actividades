import statistics
lista = input("Ingresa una lista de numeros: ").split()
lista = [int(i) for i in lista]
media = statistics.mean(lista)
print("media: ", media)
mediana = statistics.median(lista)
print("mediana: ", mediana)
moda = statistics.mode(lista)
print("moda :",moda)