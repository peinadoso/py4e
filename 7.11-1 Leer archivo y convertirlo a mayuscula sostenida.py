# Escribe un programa que lea un archivo e imprima su contenido (línea por línea), 
# todo en mayúsculas.

import os 

def convertidor(file):
    for linea in file:
        linea = str(linea)
        mayusc = linea.upper()
        print(mayusc)

# Cuando el programa pida la ruta del archivo tine que pasar con / la separacion de las 
# carpetas
archivo = str(input('Ingrese la ruta relativa del archivo: '))
fileName = open(archivo,'r')

convertidor(fileName)

