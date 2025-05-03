nums = input("Ingresa una lista de números: ").split()
nums = [int(i) for i in nums]
def promedio(nums):
    suma = sum(nums)
    cociente = len(nums)
    promedio = suma / cociente
    return promedio
print("El promedio de la lista es:", promedio(nums))