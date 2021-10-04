# Lee y analiza las líneas “From” de mbox-short.txt y extrae las direcciones de mail
# Cuenta el número de mensajes de cada persona utilizando un diccionario. Después de que
# todos los datos hayan sido leídos, imprime la persona con más envíos, creando una lista
# de tuplas (contador, email) del diccionario. Después ordena la lista en orden inverso
# e imprime la persona que tiene más envíos.

leeArchivo = input('Indica la ruta del archivo a analizar: ')
archivo = open(leeArchivo)

diccionario = dict() #Declaracion del diccionario
for lineas in archivo: #Recorro el archivo linea por linea
    if lineas.startswith('From '): #Analizo solo las lineas que comiencen con 'From'
        separada = lineas.split() #Separo cada linea que cumpla con el 'if'
        for mail in separada: #Recorro cada palabra de la linea y separo en palabras
            mail = separada[1] #Guardo la segunda palabra que es el correo 
            diccionario[mail] = diccionario.get(mail,0) + 1 #Agrego el correo al diccionario, si ya existe en el diccionario le sumo una cuenta, si no esta la agrego y le sumo uno

#Tomo todos los elementos del diccionario y lo separo en tuplas de (clave, valor)
elementos = list(diccionario.items()) 
lista = list() #Creo la lista donde guardare las tuplas del diccionario
for direccion, cantidad in elementos: #Recorro con doble variable de iteracion los elementos del diccionario separados en tuplas
    lista.append((cantidad, direccion)) #Agrego esos elementos de tuplas en la lista creada

#Ordeno la lista de tuplas de los elementos del diccionario en orden inverso
lista.sort(reverse=True)

####
# Si quiero recorrer la lista para sacar un ranking con los mejores hago un loop
# con doble variable de iteracion sobre la lista de tuplas que recorra el rango
# que quiero trabajar 

for cantidad, direccion in lista[:1]:
    print('El usuario con mas envios es:', direccion, 'con', cantidad, 'correos enviados')    


#Coursera/mbox-short.txt