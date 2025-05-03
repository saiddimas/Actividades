from temperatura import convertir_de_celcius_a_fahrenheit as CaF
from temperatura import convertir_de_fahrenheit_a_celcius as FaC
decision = input("¿Desea convertir los grados celcius o farenheit? ").lower()
if decision == "celcius":
    c = float(input("Ingrese la temperatura en grados celsius: "))
    print(f"{c} en grados farenheit son ", {CaF(c)})
elif decision == "farenheit":
    f = float(input("Ingrese la temperatura en grados farenheit: "))
    print(f"{f} en grados celsius son ", {FaC(f)})
else:
    print("Opción no válida." \
    " Por favor, elija ""celcius"" o ""farenheit"".")