from bs4 import BeautifulSoup #Importo la biblioteca beautifulsoup de la carpeta bs4 en la misma carpeta donde tengo este archivo del codigo del programa
import urllib.request, urllib.error, urllib.parse

pideURL = input('Ingrese una URL: ')
leerURL = urllib.request.urlopen(pideURL).read() #Lee la URL 
contenido = BeautifulSoup(leerURL, 'html.parser') # Guarda el contenido leido en una variable

etiquetas = contenido('span') #Defino el argumento que voy a buscar
i = 0
suma = 0
for etiqueta in etiquetas: #Recorro la pagina linea por linea
    numero = int(etiqueta.contents[0]) #Tomo el contenido de la etiqueta 'span' y lo convierto en entero de una vez
    suma += numero # Sumo cada numero encontrado
    i += 1 # Contador para determinar cuantos numeros encontro

print('\r\nSe encontraron', i, 'Numeros\r\n')
print('La suma total de los numeros es:', suma, '\r\n')

# http://py4e-data.dr-chuck.net/comments_42.html
# http://py4e-data.dr-chuck.net/comments_1334251.html