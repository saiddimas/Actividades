def obtener_elemento(lista, indice):
    try:
        elemento = lista[indice]
        return elemento
    except IndexError:
        print("Indice no existente")
        return None