num = input("Ingresa una lista de números ")

def numMayor(num):
    lista = num.split()
   
    lista1 = []
    for i in lista:
        
        lista1.append(int(i))

    lista1.sort()
    return lista1
listafinal = numMayor(num)
print(listafinal[-2])
