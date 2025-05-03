num = int(input("Ingresa un número "))
numP = True
for primo in range(2,num):
    if num % primo == 0:
        numP = False
        break
if numP:
    print("Tu número es primo")
else:
    print("Tu número no es primo")