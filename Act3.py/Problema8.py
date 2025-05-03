txt1 = str(input("Ingresa un texto "))
txt2 = txt1.lower()
txt = txt2.replace(" ", "")
def palindromo(txt):
    txtp = ""
    for i in range(len(txt)-1, -1, -1):
        txtp += txt[i]
        
    if txtp == txt:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")
palindromo(txt)