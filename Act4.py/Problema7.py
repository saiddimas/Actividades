nombre1 = input("Ingresa tu nombre completo: ")
nombre = nombre1.split()
tamano = len(nombre)
if tamano == 4:
    primer_nombre = nombre[0]
    segundo_nombre = nombre[1]
    apellido1 = nombre[2]
    apellido2 = nombre[3]
    iniciales = primer_nombre[0] + segundo_nombre[0] + apellido1[0] + apellido2[0]
    iniciales = iniciales.upper()
elif tamano == 3:
    primer_nombre = nombre[0]
    
    apellido1 = nombre[1]
    apellido2 = nombre[2]
    iniciales = primer_nombre[0] + apellido1[0] + apellido2[0]
    iniciales = iniciales.upper()
print("Tu nombre es: ", iniciales)

