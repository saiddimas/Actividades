num = int(input("Ingresa un número: "))
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else: 
        for i in range(1, num):
            num *= i
        return num
print(factorial(num))

