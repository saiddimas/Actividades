import requests
import json
ciudad = input("Ingresa la ciudad: ")
URL = f"https://api.openweathermap.org/data/2.5/forecast?q={ciudad}&appid=1823cc67e97f8840ac1894208aa88603&units=metric"
respuesta = requests.get(URL)
respuesta.raise_for_status()
datos = respuesta.json()    
dic = {}
for i in datos["list"]:
    fecha = i["dt_txt"].split()[0]
    mini = i["main"]["temp_min"]
    maxi = i["main"]["temp_max"]
    if fecha not in dic:
        dic[fecha] = {"Minimas": [], "Maximas": []}
    dic[fecha]["Minimas"].append(mini)
    dic[fecha]["Maximas"].append(maxi)
for fecha, temperaturas in dic.items():
    tmp_min = min(temperaturas["Minimas"])
    tmp_max = max(temperaturas["Maximas"])
    print(f"Dia {fecha}")
    print(f"Temperatura minima {tmp_min}")
    print(f"Temperatura maxima {tmp_max}")
with open("pronostico.json", "w") as archivo:
    json.dump(dic, archivo)