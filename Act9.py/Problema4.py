num = int(input("Ingresa un número: "))
def factorial(num):
    if num == 0 or num == 1:
        print("El factorial es 1")
    elif num < 0:
        print("El factorial no existe, ingresalo positivo porfavor")
    else:
        factorial = 1 
        for i in range(1, num + 1):
            factorial *= i
        return factorial
print("El factorial de", num, "es", factorial(num))