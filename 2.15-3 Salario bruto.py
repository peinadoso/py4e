# Escribe un programa para pedirle al usuario el número de horas y la tarifa por hora para calcular 
# el salario bruto.

def salario(horas, tarifaHoras):
    bruto = horas*tarifaHoras
    return bruto

while True:
    cantidadHoras = input('Ingrese la cantidad de horas trabajadas: ')
    tarifa = input('Ingrese el valor de cada hora: ')
    
    if cantidadHoras == 'salir' or tarifa == 'salir':
        break
    else:
        try:
            cantHoras = float(cantidadHoras)
            tarifaXHora = float(tarifa)
        except:
            print('Solo se aceptan numeros | Intente nuevamente')
            continue

        cobrar = salario(cantHoras, tarifaXHora)
        print(f'El Sueldo a cobrar por {cantHoras} trabajadas es de ${cobrar}')

print('PROGRAMA TERMINADO')
    
