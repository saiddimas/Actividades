from conversor_unidades import ConversorUnidades
unidad = input("¿Qué unidad desea convertir? ").lower()
conversor = ConversorUnidades()
if unidad == "metros":
    metros = int(input("Ingrese la cantidad de metros: "))
    metros_pies = conversor.metros_a_pies(metros)
    print(metros_pies) 
elif unidad == "kilogramos":
    kg = int(input("Ingresa la cantidad de kilogramos: "))
    kg_lb = conversor.kilogramos_a_libras(kg)
    print(kg_lb)
elif unidad == "celsius" or unidad == "celcius":
    grados = int(input("Ingresa la cantidad de grados celsius: "))
    celcius_farenheit = conversor.celsius_a_fahrenheit(grados)
    print(celcius_farenheit)
elif unidad == "litros":
    litros = int(input("Ingresa la cantidad de litros: "))
    l_a_g = conversor.litros_a_galones(litros)
    print(l_a_g)
elif unidad == "metros cuadrados":
    m2 = int(input("Ingresa la cantidad de metros cuadrados: "))
    m2_p2 = conversor.metros_cuadrados_a_pies_cuadrados(m2)
    print(m2_p2)
elif unidad == "kilometros":
    km = int(input("Ingrese la cantidad de kilometros: "))
    km_mll = conversor.kilometros_a_millas(km)
    print(km_mll)
else:
    print("Unidad no válida")