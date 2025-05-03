print("Agrega una palabra con su traducción")
dic = {}
while True:
    palabra = str(input("Ingresa una palabra: "))
    traduccion = str(input("Ingresa la traduccion de la palabra: "))
    dic = {}
    dic[palabra] = traduccion
    print("La palabra ", palabra, "se ha agregado con la traducción: ", dic[palabra])
    decision = str(input("¿Quieres agregar otra palabra? ")).lower()
    if decision == "no":
        print("Un placer")
        break
