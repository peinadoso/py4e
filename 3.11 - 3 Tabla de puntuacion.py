# Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la puntuación está fuera de ese rango
# muestra un mensaje de error. Si la puntuación está entre 0.0 y 1.0, muestra la calificación usando la 
# tabla siguiente: 
# >= 0.9 Sobresaliente
# >= 0.8 Notable
# >= 0.7 Bien
# >= 0.6 Suficiente
# < 0.6 Insuficiente

def puntuacion(puntaje):
    if puntaje >= 0.9 and puntaje < 1.1:
        print(f'{puntaje} es Sobresaliente')
    elif puntaje >=0.8 and puntaje < 0.9:
        print(f'{puntaje} es Notable')
    elif puntaje >= 0.7 and puntaje < 0.8:
        print(f'{puntaje} es Bien')
    elif puntaje >= 0.6 and puntaje < 0.7:
        print(f'{puntaje} es Suficiente')
    elif puntaje >= 0.0 and puntaje < 0.6:
        print(f'{puntaje} es Insuficuente')
    else:
        print('Estas fuera de rannnnnkinnnnnng')

while True:
    try:
        ingreso = float(input('Ingrese su puntuacion: '))
        puntuacion(ingreso)
    except:
        print('No se permite el ingreso de texto | PROGRAMA TERMINADO')
        quit()
        
