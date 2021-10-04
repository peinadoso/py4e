# Crea un programa para extraer y contar las etiquetas de párrafo (p) del documento HTML
# recuperado y mostrar el total de párrafos como salida del programa. No muestres el
# texto de los párrafos, sólo cuéntalos. Utiliza beautifulsoup

import urllib.error, urllib.parse, urllib.request
from bs4 import BeautifulSoup
import ssl


# Ignorar errores de paginas que usen certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    pideURL = input('Ingrese una URL para analizar: ')
    if pideURL == 'fin':
        print('\r\nPROGRAMA TERMINADO\r\n')
        break

    try:
        html = urllib.request.urlopen(pideURL, context=ctx).read() 
        sopa = BeautifulSoup(html, 'html.parser')

        # Recuperar todas las etiquetas de parrafos
        etiquetas = sopa('p')
        i = 0
        for etiqueta in etiquetas:
            i += 1
        
    except:
        print('URL malformada, ingrese una direccion valida')
        continue

    print('\r\n',i, 'Etiquetas <p> encontradas\r\n')

#    print(etiqueta.get('href', None))
#http://www.dr-chuck.com