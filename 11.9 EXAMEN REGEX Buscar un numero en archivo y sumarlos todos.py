import re

pideRuta = input('Indique la ruta del archivo a analizar: ')
manejador = open(pideRuta)

sumatoria = 0
i = 0
for linea in manejador:
    numero = re.findall('([0-9]+)', linea)
    elementos = len(numero)
    if elementos > 0:
        for valor in numero:
            valor = int(valor)
            sumatoria = sumatoria + valor
            i = i + 1

print('Se encontraron', i, 'valores')
print(f'La suma de todos los valores es: {sumatoria}')

#Coursera/EXAMEN regex_sum_1334249.txt