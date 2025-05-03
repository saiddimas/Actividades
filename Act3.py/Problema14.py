coeficientes = input("Ingresa los coeficientes del polinomio ")
variable = int(input("Ingresa el valor para x "))
listav = []
coeficientesorden = coeficientes.split()
for coeficientes in coeficientesorden:
    listav.append(int(coeficientes))
def polinomio(listav, variable):
    resultado = 0
    for i, a in enumerate(listav):
        resultado += a * (variable ** i)
    return resultado
resultado = polinomio(listav, variable)
print(f"El resultado del polinomio es {resultado}")
