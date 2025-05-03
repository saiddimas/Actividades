def obtener_valor(diccionario, clave):
    try:
        valor = diccionario[clave]
        return valor
    except KeyError:
        print("Clave no encontrada")
        return None
    