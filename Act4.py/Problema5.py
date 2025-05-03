txt = str(input("Ingresa un texto "))
num = int(input("ingresa el número de desplazamiento "))
def caesar(txt, num): 
    resultado = ""
    for i in txt:
        if i.isalpha() == True:
            if i.islower():
                nuevotxt = ord(i) + num
                if nuevotxt > 122:
                    nuevotxt = nuevotxt - 26
                nuevotxt = chr(nuevotxt)
                resultado += nuevotxt
            elif i.isupper():
                nuevotxt = ord(i) + num
                if nuevotxt > 90:
                    nuevotxt = nuevotxt - 26
                nuevotxt = chr(nuevotxt)
                resultado += nuevotxt
        else:
            resultado += i
    return resultado
print(caesar(txt, num))