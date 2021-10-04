# Escribe un programa que lea repetidamente números hasta que el usuario introduzca “fin”. 
# Una vez se haya introducido “fin”, muestra por pantalla el total, la cantidad de números y la media 
# de esos números. Si el usuario introduce cualquier otra cosa que no sea un número, detecta su fallo
# usando try y except, muestra un mensaje de error y pasa al número siguiente.

total=0
i=0
average=0
numero = 0

while True:
    numero = input('Ingrese un numero entero: ')
    
    if numero == 'fin': # Aca tuve que colocar el if de string antes porque me daba error 
        print(f'El total es: {total}')
        print(f'La cantidad de numeros insertados es: {i}')
        print(f'El promedio de las cantidades es: {average}')
        quit()
    else: 
        try:
            total = int(total) + int(numero)
            i = i + 1
            average = total/i
        except:
            print('Solo se admiten numeros enteros')
            continue