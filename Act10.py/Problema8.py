def convertir(cadena):
    try:
        numero = int(cadena)
        return numero
    except ValueError:
        print("Porfavor, que la cadena sea uno/varios número")
        return None
