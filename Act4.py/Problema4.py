txt = str(input("Ingresa un texto con muchos espacios "))
while "  " in txt:
    txt = txt.replace("  ", " ")
print(txt)