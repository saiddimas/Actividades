txt_viejo = str(input("Ingresa un texto: "))
txt = txt_viejo.split()
def orden_palabras(txt):
    txt.sort(key=len)
    return txt
print("El texto ordenado es: ", orden_palabras(txt))