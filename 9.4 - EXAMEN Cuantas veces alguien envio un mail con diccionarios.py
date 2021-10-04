# Escribe un programa que lea mbox-short.txt y determine quien envio el mayor numero 
# de mails. El programa busca las lineas iniciadas en 'From ' y toma la segunda palabra
# de esa lista como el emisor del mail. Crea un diccionario que mapee al emisoe del mail
# a un conteo del numero de veces que aparece en el archivo. Cuando esta finalmente armado
# el diccionario el programa lo lee y usa un loop para encontrar el maximo de apariciones

pideArchivo = input('Indique la ruta del archivo: ')
archivo = open(pideArchivo)

apariciones = dict()

for lineas in archivo:
    if lineas.startswith('From '):
        separado = lineas.split()
        emisor = separado[1]
        apariciones[emisor] = apariciones.get(emisor,0) + 1

maximo = 0
for clave in apariciones:
    if apariciones[clave] > maximo:
        maximo = apariciones[clave]
        mayor = max(apariciones, key=apariciones.get)

print(mayor, maximo)

#Coursera/mbox-short.txt