def es_palindromo(cadena):
    cadena = cadena.replace(" ", "")  # Reemplaza espacios por vacío
    cadena = cadena.lower()  # Hace todo minúscula
    cadena2 = ""
    n = len(cadena)
    # For recorre de forma inversa cada letra
    for i in range(len(cadena)-1, -1, -1):
        cadena2 = cadena[i] + cadena2  # Concatenamos la letra al inicio
    return cadena == cadena2  # Comparamos si son iguales

resultado = es_palindromo("Anita lava la tina")
print("¿Es palíndromo?", resultado)
