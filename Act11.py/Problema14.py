import requests
coordenadas = {
    "Monterrey": (25.675, -100.3161),
    "Nueva York": (40.7128, -74.0060),
    "Londres": (51.5074, -0.1278),
    "París": (48.8566, 2.3522),
    "Tokio": (35.6762, 139.6503)
}
for ciudad, coords in coordenadas.items():
    print(f"Ciudad: {ciudad}, coordenadas(latitud/longitud): {coords}")
latitud = input("Ingresa la latitud de la ciudad: ")
longitud = input("Ingresa la longitud de la ciudad: ")
url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat={latitud}&lon={longitud}&appid=1823cc67e97f8840ac1894208aa88603"
try:
    respuesta = requests.get(url)
    respuesta.raise_for_status()
    data = respuesta.json()
    aire_calidad = data["list"][0]["main"]["aqi"]
    print(f"La cálidad del aire es {aire_calidad}")
    if aire_calidad == 1:
        print("Es una buena calidad del aire")
    elif aire_calidad == 2:
        print("Es una cálidad del aire moderada")
    elif aire_calidad == 3:
        print("El aire es insalubre para grupos sencibles")
    elif aire_calidad == 4:
        print("La cálidad del aire es insalubre")
    elif aire_calidad == 5:
        print("La cálidad del aire es demasiado insalubre") 
except requests.exceptions.RequestException as e:
    print(f"Erro de conexión al obtener los datos: {e}")
