import requests
ciudad = input("Ingresa la ciudad: ")
URL = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid=1823cc67e97f8840ac1894208aa88603&units=metric"
try:
    respuesta = requests.get(URL)
    respuesta.raise_for_status()
    datos = respuesta.json()
    if respuesta.status_code == 200:
        print(f"La húmedad es : ", {datos["main"]["humidity"]})
        print(f"la temperatura es de :", {datos["main"]["temp"]})
        print(datos["weather"][0]["description"])
    else:
        print("No se pudo obtener el clima de esa ciudad")
except requests.exceptions.RequestException as e:
    print(f"Hubo un error al conectar con la API {e}")
except KeyError:
    print("No se encontraron los datos correctos en la respuesta. Verifica el nombre de la ciudad.")

