import requests
ciudad = input("Ingresa la ciudad: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid=1823cc67e97f8840ac1894208aa88603&units=metric"
try:
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    data = respuesta.json()
    latitud = data["coord"]["lat"]
    longitud = data["coord"]["lon"]
    print(f"La latidud de {ciudad} es {latitud} y su longitud es {longitud}")
except ValueError:
    print("Ciudad no encontrada")
except requests.exceptions.RequestException as e:
    print(f"Ocurrio un error de conexcion al obtener los datos: {e}")
