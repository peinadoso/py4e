# Escribe un programa que busque líneas en la forma: 'New Revision: 39772'
# Extrae el número de cada línea usando una expresión regular y el método findall(). 
# Registra el promedio de esos números e imprímelo.

import re

#Pido la ruta y abro el manejador del archivo a analizar
pideRuta = input('Ingrese la ruta del archivo: ')
handler = open(pideRuta,'r')

#Declaro las variables a usar
i = 0
sumatoria = 0.0

#Recorro linea a linea el archivo | Busco todas las lineas que comiencen con '^New Revision: '
#Busco todas las coincidencias de New Revision y un numero del 0-9 seguido de punto y 
#mas caracteres | Esa busqueda la asigno a la variable 'numero' la cual es devuelta en forma
#de lista | luego sumo lo que ya tengo + el nuevo valor, como es una lista debo cambiarlo
#a float de la forma alli descrita | Sumo un contador
for linea in handler:
    if re.search('^New Revision: ', linea):
        numero = re.findall('^New Revision: ([0-9.]+)', linea)
        sumatoria = sumatoria + float(numero[0])
        i = i + 1

#Calculo promedio e imprimo los resultados
promedio = sumatoria / i
print(sumatoria)
print(i)
print('El promedio es: ', promedio)

#Coursera/mbox.txt
#Coursera/mbox-short.txt