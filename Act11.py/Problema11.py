import requests
url = "https://swapi.py4e.com/api/starships/"
respuesta = requests.get(url)
data = respuesta.json()
dic = {}
for nave in data["results"]:
    nave1 = nave["cargo_capacity"].replace(",", "")
    if nave1 != "unknown" and int(nave1)> 100000:
        dic[nave["name"]] = nave["model"]
for nombre, modelo in dic.items():
    print(f"Nombre: {nombre}, Modelo: {modelo}")
