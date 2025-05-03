print("Ingresa el nombre y datos del alumno")
dic = {}
while True:
    nombre = str(input("Ingresa el nombre del alumno ")).lower()
    info = str (input("Ingresa información del alumno ")).lower()
    tupla = (info,)
    dic[nombre] = tupla
    print("El alumno ", nombre, "se ha agregado con la información: ", dic[nombre])
    decision = str(input("¿Quieres agregar otro alumno? ")).lower()
    if decision == "no": 
        print("Un placer")
        break