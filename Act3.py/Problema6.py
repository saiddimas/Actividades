txt = str(input("Ingresa un texto "))

def invertir(txt):
    txtn = ""
    for i in range(len(txt)-1, -1, -1):
        txtn += txt[i]
    return txtn
print(invertir(txt))
