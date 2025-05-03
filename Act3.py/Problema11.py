a11 = int(input("Ingresa el valor a11 de la matríz "))
a12 = int(input("Ingresa el valor a12 de la matríz "))
a13 = int(input("Ingresa el valor a13 de la matríz "))
a21 = int(input("Ingresa el valor a21 de la matríz "))
a22 = int(input("Ingresa el valor a22 de la matríz "))
a23 = int(input("Ingresa el valor a23 de la matríz "))
a31 = int(input("Ingresa el valor a31 de la matríz "))
a32 = int(input("Ingresa el valor a32 de la matríz "))
a33 = int(input("Ingresa el valor a33 de la matríz "))
def det(a11, a12, a13, a21, a22, a23, a31, a32, a33):
    det = a11 * (a22 * a33 - a23 * a32) - a12 * (a21 * a33 - a23 * a31) + a13 * (a21 * a32 - a22 * a31)
    return det
print("El determinante es " + str(det(a11, a12, a13, a21, a22, a23, a31, a32, a33)))
det(a11, a12, a13, a21, a22, a23, a31, a32, a33)