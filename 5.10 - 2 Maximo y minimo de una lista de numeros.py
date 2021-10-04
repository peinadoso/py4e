# Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. 
# Una vez se haya introducido “fin”, muestra por pantalla el máximo y mínimo de todos los numeros insertados
# Si el usuario introduce cualquier otra cosa que no sea un número, detecta su fallo
# usando try y except, muestra un mensaje de error y pasa al número siguiente.


minimo = None
maximo = 0

while True:
    ingreso=input('Ingrese un numero entero: ')

    if ingreso == 'fin' or ingreso == 'Fin':
        break

    try:
        numero = int(ingreso)
    except:
        print('Ingrese solamente numeros No se admiten letras o caracteres especiales')
        continue

    if numero > maximo:
        maximo = numero
    else:
        if minimo is None or numero < minimo:
            minimo = numero

        
print(f'El numero mas alto fué: {maximo}')
print('El numero mas bajo fué: ', minimo)