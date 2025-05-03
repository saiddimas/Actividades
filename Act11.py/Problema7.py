import requests
import re
url = "https://swapi.py4e.com/api/people/"
respuesta = requests.get(url)
datos = respuesta.json()
personajes = []
for personaje in datos["results"]:
    personajes.append(personaje)

patron = "^L"
nombreL = []
for personaje in personajes:
    if re.match(patron, personaje["name"]):
        nombreL.append(personaje)
dic = {}     
#alturas = []  
#for personaje in nombreL:
 #   alturas.append(personaje["height"])
for i, personaje in enumerate(nombreL):
    dic[i] = {"Nombre": personaje["name"], "Altura": personaje["height"] }
print(dic)
