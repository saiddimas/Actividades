txt = str(input("Ingresa un texto :")).lower().split()
dic = {}
for i in txt:
    if i not in dic:
        dic[i] = 1
    else: 
        dic[i] += 1
print(dic)