print("Ingresa distintos puntos del plano")
def ordenamiento():
    lista_tuplas = []
    dic = {}
    while True:
        pnto1 = input("Ingresa un punto del plano: ").split()
        pnto = [int(i) for i in pnto1]
        x = pnto[0]
        y = pnto[1]
        tupla1 = (x, y)
        lista_tuplas.append(tupla1)
        decision = input("¿Quieres agregar otro punto? ")
        if decision == "no":
            break
  

    for i in lista_tuplas:
        calculo = (i[0]**2 + i[1]**2)**0.5
        dic[calculo] = i
        
    return [valor for clave, valor in sorted(dic.items())]

print("Los puntos ordenados son: ", ordenamiento())
