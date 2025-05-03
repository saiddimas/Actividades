def suma(num):
    if num == 1:
        return 1
    else:
        return num + suma(num - 1)
num = int(input("Ingresa un número: "))
print(suma(num))