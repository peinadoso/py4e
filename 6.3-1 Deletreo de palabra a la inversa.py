# Escribe un bucle while que comience con el último carácter en la cadena y haga un recorrido hacia atrás
# hasta el primer carácter en la cadena, imprimiendo cada letra en una línea independiente.


def recorrido(word):
    # Calculo el tamaño de la palabra en numeros
    tamaño = len(word) 
    
    # Iteracion para recorrer el tamaño de la palabra de atras hacia adelante 
    for letra in word:
        tamaño = tamaño - 1 # Recorrido inverso, tomo el tamaño de la palabra y por cada iteracion le resto 1
        print(word[tamaño]) # Los corchetes son para indicar la letra que se mostrara por cada valor de tamaño
        

while True:
    palabra = input('Ingrese una palabra: ')
    
    if palabra == 'fin':
        break
    else:
        recorrido(palabra)
    

print('PROGRAMA TERMINADO')