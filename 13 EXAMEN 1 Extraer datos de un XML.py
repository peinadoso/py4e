import xml.etree.ElementTree as ET
import urllib.error, urllib.parse, urllib.request

pideURL = input('Indique el URL a analizar: ')
abreURL = urllib.request.urlopen(pideURL).read()

arbol = ET.fromstring(abreURL)
listaComments = arbol.findall('comments/comment')

sumatoria = 0
for elemento in listaComments:
    numero = int(elemento.find('count').text)
    sumatoria = sumatoria + numero

print(sumatoria)


# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_1334253.xml