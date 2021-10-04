# Pide al usuario una lista de números e imprime el máximo y el mínimo de los números 
# al final cuando el usuario ingresa “hecho”. Escribe el programa para almacenar los 
# números que el usuario ingrese en una lista, y utiliza las funciones max()
# y min() para calcular el máximo y el mínimo después de que el bucle termine.

listaNumero = list()
i = 0

def maxymin(listinNumeros):
    print('Se introdujeron', i, 'numeros')
    print(f'El numero mas bajo es: {min(listinNumeros)}')
    print(f'El numero mas alto es: {max(listinNumeros)}')
    

while True:
    numero = input('Ingrese un numero entero: ')
    if numero == 'hecho':
        break
    else:
        try: 
            entero = int(numero)
            listaNumero.append(entero)
            i = i + 1
        except:
            print('Debe ingresar solo numeros enteros | Vuelva a intentarlo')
            continue

maxymin(listaNumero)


