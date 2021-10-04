# Pedir una direccion en el mapa, contactar un servicio web y extraer el JSON para el servicio 
# web, luego analizar estos datos, se debe extraer el primer place_id del JSON 
# API a usar = http://py4e-data.dr-chuck.net/json?
# Direccion a usar =  University of Birmingham

from json import decoder
import urllib.request, urllib.parse, urllib.error
import json

claveAPI = False

if claveAPI is False:
    claveAPI = 42
    serviceURL = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceURL = 'https://maps.googleapis.com/maps/api/geocode/json?'

direccion = input('Indique una direccion: ')
parametros = dict()
parametros['address'] = direccion

if claveAPI is not False:
    parametros['key'] = claveAPI

url = serviceURL + urllib.parse.urlencode(parametros)
abreURL = urllib.request.urlopen(url)
decodificador = abreURL.read().decode()

archivo = json.loads(decodificador)

# print(json.dumps(archivo, indent=4))

lugarID = archivo['results'][0]['place_id']

print(lugarID)