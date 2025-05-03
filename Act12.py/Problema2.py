nr1 = float(input("Introduce la parte real del primer numero complejo "))
nc1 = float(input("Introduce la parte compleja del primer numero complejo "))
NC1 = complex(nr1, nc1)
nr2 = float(input("Introduce la parte real del segundo numero complejo "))
nc2 = float(input("Introduce la parte compleja del segundo numero complejo "))
NC2 = complex(nr2, nc2)
suma = NC1 + NC2
resta = NC1 - NC2
print(f"La suma es {suma} y la resta es {resta} ")