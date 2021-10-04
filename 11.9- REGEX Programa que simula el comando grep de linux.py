# Escribe un programa simple que simule la operación del comando grep en Unix. 
# Debe pedir al usuario que ingrese una expresión regular y cuente el número de líneas 
# que coincidan con ésta | Usa el archivo mbox.txt  

##################################################
#### SOLO FUNCIONA LA PRIMERA VEZ | ARREGLAR #####
##################################################

#Importo la libreria de 'Regular Expressions'
import re 

pideRuta = input('Indique la ruta del archivo a analizar: ')
manejador = open(pideRuta,'r')

contador = 0
def procesador(archivo, comando): #Funcion para buscar la expresion en el archivo
    comando = str(comando) #Declaro el comando como string para que lo tome la funcion re.search 
    global contador 
    for linea in archivo: #Recorro el archivo linea por linea
        linea = linea.rstrip() #Elimino los espacios del final de la linea
        
        #Si encuentro una 'linea' que comience con el 'comando' dado entonces aumento el contador
        if re.search(comando, linea): 
            contador = contador + 1
    return contador #Devuelvo el valor final del contador

while True:
    expresion = input('Ingrese una expresion regular | Escriba "fin" para salir: ')
    if expresion == 'fin':
        print('...HASTA LUEGUITO')
        break
    else:
        #Siempre que uso el return en una funcion debo llamar a la funcion asignadole
        #una variable para poder leer el valor del return
        veces = procesador(manejador, expresion)
        print(f'La expresion {expresion} fue encontrada {veces} veces en {pideRuta}')
        continue

#Coursera/mbox-short.txt
#Coursera/mbox.txt