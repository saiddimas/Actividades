txt = str(input("Ingresa un texto "))
def contador(txt):
    contV = 0
    contC = 0
    for i in txt:
        if i in "aeiouAEIOUáéíóúÁÉÍÓÚ":
            contV += 1
        elif i in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
            contC += 1
    return contV, contC
contador(txt)
vocales = contador(txt)[0]
consonantes = contador(txt)[1]
print("Vocales: ", vocales)
print("Consonantes: ", consonantes)