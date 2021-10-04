#Este programa almacena el nombre del dominio (en vez de la dirección) desde donde 
# fue enviado el mensaje. Al final, imprime el contenido de tu diccionario

pideArchivo = input('Indique la ruta del archivo a analaizar: ')
archivo = open(pideArchivo)

direccion = dict()

for linea in archivo:
    if linea.startswith('From '):
        separado = linea.split()
        mail = separado[1]
        dominio = mail.find('@')
        cola = mail[dominio+1:]
        direccion[cola] = direccion.get(cola,0) + 1

print(direccion)


#Coursera/mbox-short.txt



            