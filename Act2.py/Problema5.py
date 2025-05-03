
c = str(input("Ingresa un texto "))
vo = 0
v = "aeiouAEIOU"
for caracter in c:
    if caracter in v:
        vo += 1
print(c, "Tiene", vo,"vocales")
     