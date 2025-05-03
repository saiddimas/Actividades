info = {}
while True:
    materias = {}
    amigos = []
    nombre = input("Ingrese el nombre del estudiante: ")
 
    numaterias = int(input("Ingresa la cantidad de materias: "))
    for i in range(numaterias):
        materia = input("Ingresa el nombre de la materia: ")
        calificacion = float(input("Ingresa la calificacion: "))
        materias[materia] = calificacion
    num_amigos = int(input("Ingresa la cantidad de amigos: "))
    for i in range(num_amigos):
        amigo = input("Ingresa el nombre del amigo: ")
        amigos.append(amigo)    
    info[nombre] = {"materias": materias, "amigos": amigos}
    decision = input("¿Desea continuar? ").lower()
    if decision == "no":
        print("Gracias por usar el programa")
        break
