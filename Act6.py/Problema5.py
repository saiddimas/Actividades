cadena1 = str(input("Ingresa un texto: "))
cadena = cadena1.lower()
def verificador(cadena):
    vocales = ["a", "e" , "i" , "o" , "u"]
    conjuntovacio = set()
    conjunto = set()
   
    for i in cadena:
        if i.isalpha() and i not in vocales:
            conjunto.add(i)
        else: 
            conjuntovacio.add(i)
    return conjunto
print("Las consonantes que aparecen son: ", verificador(cadena))
