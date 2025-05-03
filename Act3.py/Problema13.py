año = int(input("Ingreasa un año "))
def año_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")  
año_bisiesto(año)
