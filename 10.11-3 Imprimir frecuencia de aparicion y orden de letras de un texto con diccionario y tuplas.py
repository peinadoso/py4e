# Escribe un programa que lee un archivo e imprime las letras en order decreciente de
# frecuencia. El programa debe convertir todas las entradas a minúsculas y contar
# solamente las letras a-z. El programa no debe contar espacios, dígitos, signos
# de puntuación, o cualquier cosa que no sean las letras a-z.

#Importo esta biblioteca que contiene la funcion 'string.punctuation'
import string

pideArchivo = input('Indique la ruta del archivo a analizar: ')
manejador = open(pideArchivo, 'r')

diccionario = dict()
for lineas in manejador: #recorro todo el texto linea a linea
    lineas = lineas.rstrip() #Elimino los espacios del final derecho 
    lineas = lineas.lower() #Todo el texto lo paso a minusculas
    #Elimino los signos de puntuacion de todo el texto
    lineas = lineas.translate(lineas.maketrans('', '', string.punctuation))
    lineasSeparadas = lineas.split() #Separo el texto completo en lineas
    for palabras in lineasSeparadas: #Recorro las palabras de las lineas
        for letras in palabras: #Recorro las letras de las palabras
            #Si no esta en el diccionario, lo agrego y le sumo 1 y si esta simplemente
            #le sumo 1
            diccionario[letras] = diccionario.get(letras,0) + 1

#Leo todos los items (clave, valor) del diccionario, los asigno a la variable 'elementos'
#que los devuelve en forma de tuplar a la lista elementos
elementos = list(diccionario.items()) 
listaLetras = list() 
#Recorro los 'elementos' leyendo con doble variable de iteracion (clave, valor) 
for etiqueta, valor in elementos: 
    listaLetras.append((valor, etiqueta)) #Cada elemento leido es agregado a la lista

listaLetras.sort(reverse=True) #Ordeno la lista creada en forma decreciente

#Imprimo en lineas separadas con un 'for' y ademas con doble clave de iteracion para
#que me pueda mostrar (clave, valor) de la lista de las tuplas
for clave, valor in listaLetras:
    print(clave, valor)








    



#Coursera/romeo.txt
#Coursera/words-short.txt