
texto = input("Ingresé un texto ")
i = ""
k = len(texto) - 1
while k >= 0:
    i += texto[k]
    k -= 1
print(i)