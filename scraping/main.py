from scrapingLinks import obtenerEnlacesPagina

url = 'https://cryptoslate.com/top-news/'
enlaces = obtenerEnlacesPagina(url)

if enlaces:
    for enlace in enlaces:
        print(enlace)
else:
    print("No se encontraron enlaces")