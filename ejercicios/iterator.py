# Escribe una  instruccion for  que utiliza este  iterador para imprimir las longitudes del  contenido de cada una de las paginas Web en la lista.




import urllib

Urls = [
    'http://yahoo.com',
    'http://python.org',
    'http://gimp.org',
    ]

def w(url_list):
    for url in url_list:
        f = urllib.urlopen(url)
        s = f.read()
        f.close()
        yield s
