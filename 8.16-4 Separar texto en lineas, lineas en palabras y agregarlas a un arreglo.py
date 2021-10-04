# Open the file romeo.txt and read it line by line. For each line, split the line into
# a list of words using the split() method. The program should build a list of words.
# For each word on each line check to see if the word is already in the list and
# if not append it to the list. When the program completes, sort and print the 
# resulting words in alphabetical order. 
# You can download the sample data at http://www.py4e.com/code3/romeo.txt

from os import close

pideRuta = input('Ingrese la ruta del archivo a analizar: ')
texto = open(pideRuta,'r')

consolidado = list() # Declarar una variable como lista

for linea in texto:
    listaPalabras = linea.split() # Separar cada linea del texto en una lista
    for palabras in listaPalabras: 
        if palabras in consolidado: #Buscas cada palabra en la lista 
            continue                # Si ya existe la palabra no haces nada
        consolidado.append(palabras)# Si no existe la agregas

consolidado.sort()                  #Ordena alfabeticamente los elementos de una lista
print(consolidado)


texto.close()

