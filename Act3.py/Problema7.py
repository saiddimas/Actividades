numeros = input("Ingresa una lista de números ")
numlista = []
lista = numeros.split()
for mediana1 in lista:
    numlista.append(int(mediana1))
numlista.sort()
def mediana(ordenlista):
    n = len(ordenlista)
    if n % 2 != 0:
        
        return ordenlista[n // 2]
    else:
        return (ordenlista[n // 2 - 1] + ordenlista[n // 2]) / 2

print(mediana(numlista))