# Escribe una función llamada recortar que tome una lista y la modifique, removiendo 
# el primer y último elemento y regresa None. Después escribe una función llamada medio
# que toma una lista y regresa una nueva lista que contiene todo excepto el primero
# y último elementos.

listaPalabras = list()

def recortar(listin):
    print(listin)
    largo = len(listin)
    print(f'Se eliminaran de la lista, el primer valor "{listin[0]}" y el ultimo valor "{listin[largo-1]}" ')
    del listin[largo-1]
    del listin[0] 
    print(f'La nueva lista es: {listin}')

def medio(liston):
    print(liston)
    largo = len(liston)
    print('Mostrando los valores de la lista sin el primero "',liston[0],'" ni el ultimo "',liston[largo-1],'"')
    print(liston[1:largo-1])


while True:
    palabra = input('Ingrese una palabra corta: ')
    if palabra == 'fin':
        break
    else:
        listaPalabras.append(palabra)

eleccion = int(input('Elija como desea ver la lista, escriba (1) para recortada o (2) para medio: '))
if eleccion == 1:
    recortar(listaPalabras)
elif eleccion == 2:
    medio(listaPalabras)
else:
    print('Debe elegir el numero 1 o el 2')

