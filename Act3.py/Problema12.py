lista_numeros = input("Ingresa uma lista de números ")
lista_pespacios = lista_numeros.split()
lista_n = []
for num in lista_pespacios:
    lista_n.append(int(num))
def moda(lista_n):
    dic = {}
    for i in lista_n:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    max_frecuencia = max(dic.values())
    return [k for k, v in dic.items() if v == max_frecuencia]
print(moda(lista_n))