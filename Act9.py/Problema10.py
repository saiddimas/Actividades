from vector_3d import Vector3D
vector1 = input("Ingresa las coordenadas del primer vector: ").split()
vector1 = [int(i) for i in vector1]
x, y, z = vector1
v1 = Vector3D(x, y ,z)
vector2 = input("Ingresa las coordenadas del segundo vector: ").split()
vector2 = [int(i) for i in vector2]
x2, y2, z2 = vector2
v2 = Vector3D(x2, y2 ,z2)
decision = input("¿Qué operación desea realizar? ").lower()
if decision == "suma":
    suma = v1.suma(v2)
    print(f"La suma de los vectores es {suma.x}, {suma.y}, {suma.z}")
elif decision == "resta":
    resta = v1.resta(v2)
    print(f"La resta de los vectores es {resta.x}, {resta.y}, {resta.z}")
elif decision == "producto" or decision == "producto escalar":
    producto = v1.producto_escalar(v2)
    print(f"El producto escalar de los vectores es {producto}")
elif decision == "Longitud":
    longitud = v1.modulo()
    print(f"La longitud del vector 1 es {longitud}")
elif decision == "convertirlo a unitario" or decision == "unitario":
    unitario = v1.normalizar()
    print(f"El vector unitario es {unitario.x}, {unitario.y}, {unitario.z}")




