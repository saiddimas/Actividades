cant = int(input("Ingresa la cantidad de jugadores: "))
dic = {}
for i in range(cant):

    nombre = input("Ingresa el nombre del jugador: ")
    puntuacion = input("Ingresa la puntuacion del jugador: ")
    dic[nombre] = puntuacion
print("Los jugadores y sus puntuaciones son ", dic)

