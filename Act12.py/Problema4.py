from sympy import diff, symbols, limit, Function
x = symbols('x')
funcion = x**2 + 3*x +2 
limite = float(input("Ingresa el valor del límite "))
lim = limit(funcion, x, limite)
print(lim)
derivada = diff(funcion, x)
print(derivada)