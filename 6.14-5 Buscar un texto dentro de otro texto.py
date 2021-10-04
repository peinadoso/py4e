# Toma el siguiente código en Python que almacena una cadena:
# str = 'X-DSPAM-Confidence:0.8475'
# Utiliza find para extraer el numero de la cadena de texto después del carácter
# dos puntos y después utiliza la función float para convertir la cadena extraída 
# en un número de punto flotante.


def buscando(cadena):
    posicion = cadena.find(':')

    numero = cadena[posicion+1:]
    flotante = float(numero)
    print('El numero decimal es', flotante)
    print(type(flotante))
    print('PROGRAMA TERMINADO')
    quit()


print('INICIANDO EL PROGRAMA')
print('Buscando el numero decimal en la linea --> X-DSPAM-Confidence:0.8475')
string = 'X-DSPAM-Confidence:0.8475'

buscando(string)
