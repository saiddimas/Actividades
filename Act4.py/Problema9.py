txt1 = str(input("Ingresa un texto: "))
txt0 = txt1.split()
txt2 = str(input("Ingresa un texto: "))
txt4 = txt2.split()
def orden_palabras(txt0, txt4):
    orden = ""    
    txt0.sort(key=len)
    txt4.sort(key=len)
    orden = txt0 + txt4
    orden.sort(key=len)
    return orden
print("El texto ordenado es: ", orden_palabras(txt0, txt4))