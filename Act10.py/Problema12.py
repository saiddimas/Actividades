import math
def raiz_cuadrada(numero):
    try:
        resultado = math.sqrt(numero)
        return resultado
    except (ValueError, ImportError):
        print("Importación de la librería fallida ó número introducido negativo")
        return None