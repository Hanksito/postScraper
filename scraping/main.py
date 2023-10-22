from scrapingLinks import obtenerEnlacesPagina
from scrapingPost import obtenerContenidoPagina
url = 'https://cryptoslate.com/top-news/'
enlaces = obtenerEnlacesPagina(url)

if enlaces:
    for enlace in enlaces:
        obtenerContenidoPagina(enlace)
        
else:
    print("No se encontraron enlaces")