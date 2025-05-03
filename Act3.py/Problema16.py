def generar_fibonacci(n):
    fibonacci = [1, 1]  # Inicializa la lista con los dos primeros números
    while len(fibonacci) < n:
        # Se agrega el siguiente elemento a la lista
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci  # Retorna la lista

resultado = generar_fibonacci(10)  # Llamada a la función
print("Serie de Fibonacci:", resultado)
