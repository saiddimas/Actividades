x1 = float(input("Ingresa el valor de x1: "))
y1 = float(input("Ingresa el valor de y1: "))
x2 = float(input("Ingresa el valor de x2: "))
y2 = float(input("Ingresa el valor de y2: "))
punto1 = (x1, y1)
punto2 = (x2, y2)

def distancia_total(punto1, punto2):
    distancia = ((punto2[0] - punto1[0])**2 + (punto2[1] - punto1[1])**2)**0.5
    return distancia
print("La distancia entre los dos puntos es", distancia_total(punto1, punto2))