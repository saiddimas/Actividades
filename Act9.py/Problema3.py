txt = str(input("Ingresa un texto: "))
def contador(txt):
    cont_a = 0
    cont_e = 0 
    cont_i = 0
    cont_o = 0
    cont_u = 0
    for i in txt:
        if i == "a":
            cont_a += 1
        elif i == "e":
            cont_e += 1
        elif i == "i":
            cont_i += 1
        elif i == "o":
            cont_o += 1
        elif i == "u":
            cont_u += 1
    tupla = ()
    tupla = ("a", cont_a,"e", cont_e,"i", cont_i,"o", cont_o,"u", cont_u)
    return tupla
print("La cantidad de vocales es:", contador(txt))