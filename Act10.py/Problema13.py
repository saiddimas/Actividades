def dividir_elementos(lista, divisor):
    try:
        resultados = [elemento / divisor for elemento in lista]
        return resultados
    except ZeroDivisionError:
        print("Error al dividir entre 0")
        return None