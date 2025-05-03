numA = int(input("Ingresa el número menor "))
numB = int(input("Ingresa el número ayor "))
def MCD(numA, numB):

        while numA != 0:
            r = numB % numA
            numB = numA
            numA = r
        print("El MCD es ", numB)
MCD(numA, numB)