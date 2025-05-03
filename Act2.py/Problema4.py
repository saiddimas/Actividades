num = int(input("Ingresa un número del 1 al 50 "))
if 1<=num<=50:
    f1 = 0
    f2 = 1
    fibo = [f1,f2]
    for _ in range(num-2):
        ns = f1 + f2
        fibo.append(ns)
        f1,f2 = f2,ns
    print("Los primeros", num,"números de la lista de Fibonacci son")
    print(fibo[:num])
else:
    print("Tu número debe estar entre el 1 y el 50")