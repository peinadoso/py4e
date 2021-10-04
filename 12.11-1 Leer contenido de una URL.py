# Crea un programa que le pida al usuario la URL, de modo que pueda leer cualquier página
# web. Puedes usar split('/') para dividir la URL en las partes que la componen, 
# de modo que puedas extraer el nombre del host para la llamada a connect del socket.
# Añade comprobación de errores utilizando try y except para contemplar la posibilidad 
# de que el usuario introduzca una URL mal formada o inexistente.

import socket #Importo la libreria de 'Socket'

#Loop para pedir URL mientras corre el programa
while True: 
    pideURL = input('Ingresa una URL completa: ') 
    separado = pideURL.split('/') #Divido la URL en secciones cuando consiga un slash
    #Manejo de errores, si la lista 'separado' no tiene por lo menos 3 elementos
    #lanza un error y vuelve nuevamente a iniciar el While
    try:
        dominio = separado[2] #La lista siempre tomara el segundo espacio que es el host
    except: 
        print('URL mal formada, el formato debe ser http(s)://dominio | ',len(separado), 'espacio ocupado')
        continue  
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creacion del socket
    mySocket.connect((dominio, 80)) #Conexion del socket por el puerto 80
    comando = (f'GET {pideURL} HTTP/1.0\r\n\r\n').encode() #Creacion del comando a enviar
    mySocket.send(comando) #Envio del comando 
    break #Termino el loop

#Mientras haya datos para transmitir, corre este loop
while True:
    datos = mySocket.recv(512) #Recibir datos en bloques de 512 bytes
    if len(datos) < 1: #Si ya no quedan mas bytes por transferir entonces sal del loop
        break
    print(datos.decode(),end='') #Imprimir el contenido http en pantalla

mySocket.close() #Cerrar el socket      


#http://data.pr4e.org/romeo.txt