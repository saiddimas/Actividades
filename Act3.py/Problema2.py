nums = input("Ingresa una lista de números: ")
numA = []
lista = nums.split()
for nums in lista:
    numA.append(int(nums))
def suma_num(*numA):
    suma = sum(numA)    
    return suma

print(suma_num(*numA))


