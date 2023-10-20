from scrapingMain import obtener_enlaces_pagina

url = 'https://cryptoslate.com/top-news/'
enlaces = obtener_enlaces_pagina(url)

if enlaces:
    for enlace in enlaces:
        
else:
    print("No se encontraron enlaces.")