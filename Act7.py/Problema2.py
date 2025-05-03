
cant = int(input("Ingresa la cantidad de estudiantes: "))
dic = {}
for i in range(cant):

    nombre = input("Ingresa el nombre del estudiante: ")
    nota = input("Ingresa las nota del estudiante: ").split()
    nota = [float(nota[i]) for i in range(len(nota))]
    dic[nombre] = nota
    print("Las notas de ", nombre, "son: ", dic[nombre])
