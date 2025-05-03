def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def calcular_mcm(a, b):
    return (a * b) // gcd(a, b)

# Ejemplo de uso
numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa un número: "))
mcm_resultante = calcular_mcm(numero1, numero2)
print(f"El MCM de {numero1} y {numero2} es {mcm_resultante}")
#Cuál es el propósito de la función 'gcd' en el código proporcionado?
#Calcular el máximo común divisor de dos números.
#En el cálculo del MCM, ¿qué papel juega el resultado de la función 'gcd'?
#Se utiliza para dividir el producto de los números.
#Si los números ingresados son 8 y 12, ¿cuál será el resultado de 'calcular_mcm'?
#4
#Si 'x' es inicialmente 15 y 'y' es 10 en la función 'gcd', ¿cuál será el primer valor de 'x' y 'y' en la primera iteración del bucle?
#x=10, y=5
#¿Qué pasaría si se ingresara un número negativo en 'calcular_mcm'?
#El programa devolvería un error y no funcionaría.
