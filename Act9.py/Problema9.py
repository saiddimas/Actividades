from calculadora_cientifica import Calculadora_Cientifica
numero = int(input("Ingresa el número: "))
calculadora = Calculadora_Cientifica()
logaritmo = calculadora.logaritmo(numero)
print(f"El logaritmo base 10 de {numero} es {logaritmo}")
