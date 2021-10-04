# Escribe un programa para leer a través de un historial de correos, construye un 
# histograma utilizando un diccionario para contar cuántos mensajes han llegado
# de cada dirección de correo electrónico, e imprime el diccionario.
# Luego calcula e imprime que direccion envio mas mensajes y cual menos mensajes
# Usar como fuente el archivo mbox-short.txt

leeArchivo = input('Ingrese la ruta del archivo a analizar: ')
archivo = open(leeArchivo,'r')

print(' ')

direccion = dict()

#Esta implementacion es para sumar al diccionario las direcciones de mails de todo el
#archivo con la cantidad de repeticiones
for lineas in archivo:
    if lineas.startswith('From '): #Analizo las lineas que comiencen con 'From '
        lineado = lineas.split() #Divido esas lineas en lista de palabras
        mail = lineado[1] #Tomo solo el segundo valor de esa lista el cual es el mail
        #Si en el diccionario 'direccion' no existe la clave 'mail' la guardo con el metodo '.get' 
        #con un valor default de 0 y le sumo 1 al final y si ya existe le sumo 1
        direccion[mail] = direccion.get(mail, 0) + 1

#Esta implementacion es para calcular el correo mas enviado y el menos enviado
maximo = 0
minimo = 1000
for clave in direccion: #Recorro el diccionario para revisar cada 'valor'
    #Si el valor de esa clave es mayor al maximo se la asigno a 'maximo'
    if direccion[clave] > maximo:
        maximo = direccion[clave]
        #Uso la funcion 'max' para obtener la 'clave' con mayor valor de todo el diccionario 
        mayor = max(direccion, key=direccion.get) 
    if direccion[clave] < minimo:
        #Si el valor de esa clave es mayor al maximo se la asigno a 'maximo'
        minimo = direccion[clave]
        #Uso la funcion 'min' para obtener la 'clave' con mayor valor de todo el diccionario 
        menor = min(direccion, key=direccion.get)

print(direccion)
print(' ')
print('El mail con mas envios es -->', mayor, 'con', maximo, 'Envios')
print('El mail con menos envios es -->', menor, 'con', minimo, 'Envios')



print('....PROGRAMA TERMINADO')
#Coursera/mbox-short.txt