from bs4 import BeautifulSoup
import urllib.request, urllib.error, urllib.parse

pideURL = input('Ingrese una URL valida: ')
ubicacion = int(input('Ingrese el numero del enlace que quiere seguir: '))
repeticion = int(input('Indique la cantidad de veces que se repite el procedimiento: '))

abrirURL = urllib.request.urlopen(pideURL).read()
archivo = BeautifulSoup(abrirURL, 'html.parser')
etiquetas = archivo('a')

direcciones = list()
for n in range(repeticion):
    enlace = etiquetas[ubicacion-1].get('href', None)
    direcciones.append(enlace)
    abrirURL = urllib.request.urlopen(enlace).read()
    archivo = BeautifulSoup(abrirURL, 'html.parser')
    etiquetas = archivo('a')

for lineas in direcciones:
    print(lineas)
    
# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Carmen.html

