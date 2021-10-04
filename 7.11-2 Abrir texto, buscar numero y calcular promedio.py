#Pido nombre de archivo al usuario
from typing import TextIO

# Cuando el programa pida la ruta del archivo tine que pasar con / la separacion de las carpetas
fname = input('Ingrese la ruta relativa del archivo: ') 
fh = open(fname) #Abro ese archivo para trabajarlo, este es el handle

adicion = 0
promedio = 0
contador = 0 

#Este for busca linea por linea en el texto completo
for lineas in fh:
    if lineas.startswith('X-DSPAM-Confidence:'): #Busca las lineas que comiencen con ese argumento
        inicio = lineas.find('0') #Busca en cada linea encontrada el caracter '0'
        rango = lineas[inicio:] #Asigna a la variable rango los caracteres encontrados en 'inicio' y hasta el final de la linea
        #Manejo de error 
        try:
            numero = float(rango)
        except:
            print("Error del sistema | Ronny")
        
        adicion = adicion + numero #Suma de los valores encontrados en cada linea
        contador = contador + 1 #Aumento del contador que me servira para calcular el promedio

promedio = adicion / contador #Calculo del promedio
print('Average spam confidence: ',float(promedio))

