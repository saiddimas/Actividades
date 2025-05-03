txt = str(input("Ingresa un texto "))
sub_txt = str(input("Ingresa una texto subcadena "))

def contador(txt, sub_txt):
    cont = 0
    nuevo_sub = len(sub_txt)
    for i in range(0, len(txt), 1):
        if txt[i:i+nuevo_sub] == sub_txt:
            cont += 1
    return cont
print("La subcadena aparece: ", contador(txt, sub_txt), "veces")