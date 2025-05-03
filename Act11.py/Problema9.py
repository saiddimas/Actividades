import requests
url = "https://swapi.py4e.com/api/planets/"
try:
    respuesta = requests.get(url)
    data = respuesta.json()
    if respuesta.status_code == 200:
        poblacion = []
        
        for planeta in data["results"]:
            numero = planeta["population"]
            
        #for planeta in planetas:
            
            if numero != "unknown":
              
                poblacion.append(int(numero))
        if poblacion:        
            suma = sum(poblacion)
            cociente = len(poblacion)
            promedio = suma / cociente
            print(f"El número de habitantes promedio por planeta es: ", {promedio})
        else:
            print("No se encontraron planetas con población válida")
    else:
        print("Ocurrio un error inesperado")
except requests.exceptions.RequestException as e:
    print(f"Hubo un error al conectar con la API {e}")