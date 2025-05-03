import math
r = float(input("ingresa el radio :"))
angulo = float(input("ingresa el angulo en radianes :"))
tupla = (r, angulo) 
x = tupla[0] * math.cos(tupla[1])
y = tupla[0] * math.sin(tupla[1])
tupla2 = (x, y)
print("Las coordenadas rectangulares son : ", tupla2)