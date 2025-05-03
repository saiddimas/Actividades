from cifrado_cesar import CifradorCesar
accion = input("¿Deseas cifrar o descifrar un texto? ").lower()
num_desplazamiento = int(input("Ingresa el número de caracteres desplazados: "))
cifrado = CifradorCesar(num_desplazamiento)

if accion == "cifrar":
    txt = input("Ingresa el textoa a cifrar: ")
    txt_cifrado = cifrado.cifrar(txt)
    print(txt_cifrado)
elif accion == "descifrar":
    txt = input("Ingresa el texto a descifrar: ")
    txt_descifrado = cifrado.descifrar(txt)
    print(txt_descifrado)
else:
    print("Texto no válido")