# Este programa cuenta la distribución de la hora del día para cada uno de los mensajes.
# Puedes extraer la hora de la línea “From” buscando la cadena horaria y luego dividiendo
# la cadena en partes utilizando el carácter ':' Una vez que hayas acumulado las
# cuentas para cada hora, imprime las cuentas, una por línea, ordenadas por hora

pideRuta = input('Indique la ruta del archivo a analizar: ')
handler = open(pideRuta)

#Loop donde separo el texto en lineas, luego busco la posicion de ':' para saber donde 
# comienza la hora, luego tomo el rango de esa posicion para saber solo la hora
# para luego hacer una lista solo con las horas de todos los mails
listaHoras = list() 
for linea in handler:
    if linea.startswith('From '):
        posicionHora = linea.find(':')
        horario = linea[posicionHora-2:posicionHora]
        listaHoras.append(horario)

#Creo un diccionario con la lista de las horas recopiladas y si no estan las agrego y les sumo +1
diccionario = dict()
for horas in listaHoras:
    diccionario[horas] = diccionario.get(horas, 0) + 1

#Obtengo las tuplas con (clave, valor) del diccionario con el objetivo de poder ordenarlas
horaOrdenada = list()
for clave, valor in list(diccionario.items()):
    horaOrdenada.append((clave, valor))

#Ordeno las tuplas del diccionario anterior
horaOrdenada.sort()

#Imprimo en lineas separadas con un 'for' y ademas con doble clave de iteracion para
#que me pueda mostrar (clave, valor) de la lista de las tuplas
for clave, valor in horaOrdenada:
    print(clave, valor)
    

#Coursera/mbox-short.txt