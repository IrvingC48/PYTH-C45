import json
import requests

try:
    with open('Modulo_4/API_KEY.json', 'r') as file:
        API_KEY = json.load(file)['KEY']
        print("JSON loaded sucessfully.")
except FileNotFoundError:
    print("Error: The API_KEY was not found.")
    exit
except json.JSONDecodeError:
    print("Error: Failed to decoded JSON from the file (malformed JSON).")
    exit

#1. Definir la URL
base_url = 'https://api.nasa.gov/'
route_url_Neo_Feed = 'neo/rest/v1/feed'
start_date = '2026-10-01'
end_date = '2026-10-03'
url = f"{base_url}{route_url_Neo_Feed}?start_date={start_date}&end_date={end_date}&api_key={API_KEY}"

#2. Realizar la petición
response = requests.get(url)

#3. Análisis de la respuesta
if response.status_code == 200:
    with open('Modulo_4/response.json', 'w') as archivo:
        data = response.json()
        json.dump(data, archivo, ensure_ascii=False, indent=4)
        # print("guardado")

        #1. Obtiene la primera fecha del diccionario
        first_date = next(iter(data["near_earth_objects"])) #<-- next(iter(...)) extrae el primer elemento de una colección iterable 
                                                                #(como las claves de un diccionario) de forma directa en tiempo O(1), 
                                                                # sin necesidad de convertir toda la estructura en una lista en memoria. 
        print(f'Procesando fecha: {first_date}\n')

        for neo_feed in data["near_earth_objects"][first_date]: #<-- Agregamos la primera fecha para acotar el recorrido
            name = neo_feed["name"]
            dangerous = neo_feed["is_potentially_hazardous_asteroid"]
            print(f'Asteroide: {name} | ¿Es peligroso?: {dangerous}') #["estimated_diameter"]["is_potentially_hazardous_asteroid"]
else:
    print(f'Error: {response.status_code}')