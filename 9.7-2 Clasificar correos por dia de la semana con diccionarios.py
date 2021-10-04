# Escribir un programa que clasifica cada mensaje de correo dependiendo del día de la
# semana en que se recibió. Para hacer esto busca las líneas que comienzan con “From”,
# después busca por la tercer palabra y mantén un contador para cada uno de los días
# de la semana. Al final del programa imprime los contenidos de tu diccionario 
# (el orden no importa).
# Línea de ejemplo: From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
# Usar como fuente el archivo mbox-short.txt

pideArchivo = input('Indique la ruta del archivo para analizar: ')
archivo = open(pideArchivo)

mail = dict()

for lineas in archivo:
    if lineas.startswith('From '): #Analizo solo las entradas que empiezan con 'From '
        lineado = lineas.split() #Solo las que empiezan con 'From ' las divido en listas de palabras
#        print(lineado)
        dia = lineado[2] #Busco la 3era palabra de esa lista que representa el dia
        #Si en el diccionario 'mail' no existe la clave 'dia' la guardo con el metodo '.get' 
        #con un valor default de 0 y le sumo 1 al final y si ya existe le sumo 1
        mail[dia] = mail.get(dia, 0) + 1 
        

print(mail) #Imprimo el contenido completo del diccionario 
        
#Coursera/mbox-short.txt



