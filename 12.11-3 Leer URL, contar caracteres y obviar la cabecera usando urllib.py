# Utiliza urllib para rehacer el ejercicio anterior de modo que 
# (1) Reciba el documento de una URL
# (2) Muestre hasta 3000 caracteres
# (3) Cuente la cantidad total de caracteres en el documento. No te preocupes de las
# cabeceras en este ejercicio, simplemente muesta los primeros 300 caracteres 
# del contenido del documento.

import urllib.request

pideURL = input('Indique una URL completa: ')
archivo = urllib.request.urlopen(pideURL)

recibido = ''
i = 0
for linea in archivo:
    lineaDecoded = linea.decode().strip()
    recibido += lineaDecoded + '\r\n'
    for caracteres in recibido:
        i += 1

print(recibido[:300], '<- Caracter numero 300\r\n')
print('Total de caracteres en el archivo ',i,'\r\n')

#http://data.pr4e.org/intro-short.txt
