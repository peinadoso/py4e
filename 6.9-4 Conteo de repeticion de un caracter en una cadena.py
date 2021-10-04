# Escribe una programa que cuente el número de veces que una letra aparece en una palabra.

def conteo(palabra, letra):
    palabra = str(palabra)
    letra = str(letra)
    repeticion = palabra.count(letra)

    if repeticion == 1:
        print('La letra', letra, 'se repite', repeticion, 'vez')
    else:
        print('La letra', letra, 'se repite', repeticion, 'veces')

while True:
    word = input('Ingrese una cadena de texto: ')
    letter = input('Ingrese la letra para verificar cuanto se repite: ')

    if word == 'salir':
        break
    else: 
        conteo(word, letter)

print('PROGRAMA TERMINADO')

    