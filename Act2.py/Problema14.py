import random
n = int(input("Ingresa la cantidad de números aleatorios: "))
if n > 0:
    lista_aleatoria = []
    contador = 0
    while contador < n:
        num = random.randint(1, 100)
        lista_aleatoria.append(num)
        contador += 1

    print("Lista de números aleatorios:", lista_aleatoria)
else:
    print("Por favor, ingresa un número mayor que 0.")