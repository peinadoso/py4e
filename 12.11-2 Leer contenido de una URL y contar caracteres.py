# Pide una URL y cuenta el número de caracteres que ha recibido y se detenga, con un texto
# en pantalla, después de que se hayan mostrado 3000 caracteres. El programa debe
# recuperar el documento completo y contar el número total de caracteres, mostrando
# ese total al final del documento.

import socket

while True:
    pideURl = input('Ingrese una URL completa para analizarla: ')
    separar = pideURl.split('/')

    try:
        host = separar[2]
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        mySocket.connect((host, 80))
    except:
        print('Ingrese una URL con formato "https[s]://dominio/[pagina] | ',len(separar), 'Espacios en la lista')
        continue
    
    comando = (f'GET {pideURl} HTTP/1.0\r\n\r\n').encode()
    mySocket.send(comando)
    break

tamaño = 0
recibido = b'' #Declaracion de una variable tupi 'Byte'
# texto = ''
# i = 0
while True:
    datos = mySocket.recv(512)
    
    if len(datos) < 1:
        break
    
    recibido = recibido + datos #Voy sumando todos los bloques de texto recibidos
    contenido = recibido.decode()
    tamaño = tamaño + len(datos) #Suma de todos los caracteres recibidos

#Imprimo los primeros 300 caracteres
print(contenido[:300],'\r\n', 'Estos son los primeros 300 caracteres ')
print(tamaño,'CARACTERES EN TOTAL\r\n') #Imprimo los carcateres totales recibidos

##### OTRA SOLUCION #######
# for caracteres in contenido:
#     texto = texto + caracteres
#     i = i + 1

#     if i >= 299:
#         break
    
# print(texto+'\r\n')
# print(i, 'Caracteres impresos hasta aqui'+'\r\n')
# print(tamaño, 'caracteres encontrados en total'+'\r\n')
        
mySocket.close()

#http://data.pr4e.org/romeo.txt
#https://www.claretbsas.edu.ar/