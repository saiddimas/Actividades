v0 = input("Ingresa la magnitud del primer vector: ").split()
v1 = []
for i in v0:
    v1.append(int(i))
v3 = input("Ingresa la magnitud del segundo vector: ").split()
v2 = []
for i in v3:
    v2.append(int(i))
producto =  v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]
print("El producto punto es:", producto)