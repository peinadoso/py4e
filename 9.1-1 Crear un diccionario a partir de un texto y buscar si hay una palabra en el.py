# Escribe un programa que lee las palabras en words.txt y las almacena como claves en
# un diccionario. No importa qué valores tenga. Luego puedes utilizar el operador
# in como una forma rápida de revisar si una cadena está en el diccionario.

palabras = dict()
valor = 1

palabreo = input('Ingrese la ruta del archivo: ') #Pido ruta del archivo
abreArchivo = open(palabreo,'r') # Abro el archivo con el handler (open) modo "Read"

for lineas in abreArchivo: # Loop para separar texto en lineas
    divideLineas = lineas.split() 
    for words in divideLineas: # Loop para separar lineas en palabras
        palabras[words] = valor # Agrego cada palabra al diccionario y le agrego un valor
        valor = valor + 1 # Contador para saber la posicion de cada letra

print('.......ARCHIVO PROCESADO')

while True:
    # Pido una palabra para saber si existe en el texto
    existe = input('Escribe una palabra para saber si existe y cual es su posicion: ')

    if existe in palabras: # Saber si existe la palabra dentro del texto
        posicion = palabras[existe] # Asigo a "posicion" el valor encontrado en el diccionario "palabras" con la clave "existe" 
        print(f'La palabra "{existe}" existe y está en la posicion -{posicion}-')
    elif existe == 'fin':
        break
    else:
        print('Esta palabra no esta en el texto, intente con otra')
        continue

print('CHAO MUCHAS GRACIAS')

#Coursera/words-short.txt
