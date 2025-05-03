
num = input("Ingresa una lista de números con espacios ")
lista = list(map(int, num.split()))
k = 0
for n in lista:

    k += n
print("La suma de esa lista es", k)