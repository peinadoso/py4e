# Escribe un programa que calcule el salario de un trabajador pasandole la cantidad de horas trabajadas
# y el valor de cada hora, si el empleado trabaja mas de 40 horas, pagar 1.5 veces la tarifa horaria 
# para todas las horas trabajadas que excedan de 40.

def pagaMensual(horasTrabajadas, valorHora):
    if horasTrabajadas <= 40:
        cheque = horasTrabajadas * valorHora
    elif horasTrabajadas > 40:
        horasAdicionales = horasTrabajadas - 40
        valorExtra = valorHora * 1.5
        cheque = (40*valorHora) + (horasAdicionales * valorExtra)
        print(f'Trabajaste {int(horasAdicionales)} horas extras')
        print(f'Estas horas seran pagadas a ${int(valorExtra)} la hora')
    return cheque

horasT = input('Indique la cantidad de horas trabajadas: ')
valorH = input('Indique el valor de la hora: ')
try:    # Manejador de errores en caso de que ingrese texto al momento de pedir los datos por teclado
    resultado = pagaMensual(float(horasT), float(valorH)) # Se declara el tipo de variable aca porque se necesita saber si antes lee texto 
    print(f'Monto total a cobrar: ${resultado}')
except: # En caso de ingresar texto por teclado, genera un error y ejecuta este trozo de codigo
    print('Los datos ingresados solo pueden ser numeros | PROGRAMA TERMINADO')
    quit()



