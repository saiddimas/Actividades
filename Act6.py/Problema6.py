nums = input("Ingresa una lista de números: ").split()
conjunto = set(nums)
quitar = input("Ingresa el número a quitar: ")
if quitar in conjunto:
    conjunto.remove(quitar)
    print("La lista sin " + quitar + " es: " + str(conjunto))
