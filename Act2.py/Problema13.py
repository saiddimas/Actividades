c = str(input("Ingresa un texto "))
h = str(input("Ingresa la letra quer quieres ver "))
vo = 0
v = h
for caracter in c:
    if caracter in v:
        vo += 1
print(c, "Tiene", vo,"letra(s)", h)
     