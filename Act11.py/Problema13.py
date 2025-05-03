import requests
import json
url = "https://swapi.py4e.com/api/films/"
respuesta = requests.get(url)
data = respuesta.json()
dic ={}
for titulo in data["results"]:
    dic[titulo["title"]] = titulo["release_date"]
for title, fecha in dic.items():
    print(f"Titulo: {title}, fecha de lanzamiento: {fecha} ")
with open("peliculas.json", "w") as archivo:
    json.dump(dic, archivo)