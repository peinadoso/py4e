# Abre el archivo mbox-short.txt leelo linea por linea. cuando encuentres una linea 
# que comience con 'From' como por ejemplo:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Analiza la linea usando split() e imprime la segunda palabra de la linea
# (Ej. La direccion entera de la persona que envio el mail). 
# Finalmente imprime en pantalla un conteo al final.
# El resultado final debe incluir la salida del conteo como en el siguiente ejemplo
# ----> There were 27 lines in the file with From as the first word
# TIP: Asegurate de no incluir las lineas que comienzan con 'From:'

leeArchivo = input('Ingrese la ruta del archivo: ')
archivo = open(leeArchivo,'r')

conteo = 0

for linea in archivo:
    if linea.startswith('From '):
        cortada = linea.split() # Divide cada linea comenzada con 'From' en listas
        mail = cortada[1] # De cada lista toma el segundo valor que es el mail
        conteo = conteo + 1 # Este contador es para totalizar la cantidad de lineas encontradas con 'From'
        print(mail)       

print('There were', conteo, 'lines in the file with From as the first word')

#Coursera/mbox-short.txt