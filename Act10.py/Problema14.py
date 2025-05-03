def escribir_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
    except IOError:
        print("Falla en la entrada/salida de la operacion al archivo")
        return None