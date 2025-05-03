texto = input("Ingresa un texto ")
k = 0
numP = False
for cant in texto:
    if cant != ' ' and not numP:
        numP = True
        k += 1
    elif cant == ' ':
        numP = False
print("Tu texto contiene", k,"palabras")