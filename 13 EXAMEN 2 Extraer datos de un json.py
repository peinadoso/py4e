import json #Importar libreria json para decodificar archivos json
import urllib.request, urllib.error, urllib.parse #Import urllib

leerURL = input("Indique la URL a analizar: ")
#Lee la info dentro del URL, y la decodifica para tenerla en utf-8, asi es mas comprensible para
#analizarla como texto plano
abreURL = urllib.request.urlopen(leerURL).read().decode()
print(f'Accediendo a {leerURL}')
print('Extraidos', len(abreURL), 'caracteres')

#Leo el contenido del json
archivo = json.loads(abreURL)

#IMPORTANTE: Para leer los diccionarios obtenidos dentro del json debo indicarle a una variable
#A cual diccionario quiero entrar, en este caso tengo 2 diccionarios y quiero entrar al que
#tiene como primer elemento 'comments' | Chequear el url con el json para ver la estructura
diccionarios = archivo['comments']
sumatoria = 0
contador = 0
for elemento in diccionarios: #Recorro linea por linea el diccionario 'comments'
    numero = elemento['count'] #Obtengo el valor del 'key' llamado 'count'
    sumatoria = sumatoria + numero 
    contador += 1

print('Contador:', contador)
print('La suma es:', sumatoria)



# http://py4e-data.dr-chuck.net/comments_42.json
# http://py4e-data.dr-chuck.net/comments_1334254.json