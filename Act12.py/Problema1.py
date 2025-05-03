from fractions import Fraction
fraccion1 = input("Ingresa la primera fracción en formato ""numerador, denominador ").split(",")
n1 = int(fraccion1[0])
d1 = int(fraccion1[1])
fraccion2 = input("Ingresa la segunda fraccion en formato ""numerador, denominador ").split(",")
n2 = int(fraccion2[0])
d2 = int(fraccion2[1])
f1 = Fraction(n1, d1)
f2 = Fraction(n2, d2)
suma = f1 + f2
mult = f1 + f2
print(suma)
print(mult)