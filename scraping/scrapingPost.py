import requests
from bs4 import BeautifulSoup
from traslationsText import traducir

def obtenerContenidoPagina(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
        else:
            print(f"Error al hacer la solicitud. Código de respuesta: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error al obtener la página: {e}")
        return None

    if html is not None:
        soup = BeautifulSoup(html, 'html.parser')
        divPostContainer = soup.find('div', class_='post-container')

        if not divPostContainer:
            return None

        informacionPost = {
            'titulo': '',
            'subtitulo': '',
            'imgPost': '',  
            'secciones': []
        }

        
        h1 = divPostContainer.find('h1')
        if h1:
            titulo = h1.text.strip()
            informacionPost['titulo'] = traducir(titulo)

        
        pSubheading = divPostContainer.find('p', class_='post-subheading')
        if pSubheading:
            subtitulo = pSubheading.text.strip()
            informacionPost['subtitulo'] = traducir(subtitulo)

            
        img = divPostContainer.find('img', class_='nolazy')
        if img:
            imgPost = img.get('src')  
            informacionPost['imgPost'] = imgPost
        
        
        seccionActual = None
        elementos = divPostContainer.find_all(['h2', 'p'])
        for elemento in elementos:
            if elemento.name == 'h2':
                if seccionActual:
                    informacionPost['secciones'].append(seccionActual)
                seccionActual = {'titulo': traducir(elemento.text.strip()), 'parrafos': []}
            elif elemento.name == 'p':
                if seccionActual:
                    seccionActual['parrafos'].append(traducir(elemento.text.strip()))

        
        if seccionActual:
            informacionPost['secciones'].append(seccionActual)

        if not informacionPost['secciones']:
            # Si no se encontraron secciones, usar todos los párrafos como una única sección
            parrafos = divPostContainer.find_all('p')
            if parrafos:
                seccion_unica = {
                    'titulo': '',
                    'parrafos': [traducir(parrafo.text.strip()) for parrafo in parrafos]
                }
                informacionPost['secciones'].append(seccion_unica)

        return informacionPost
    else:
        print("No se pudo obtener el HTML del post-container.")

url = 'https://cryptoslate.com/sbf-trial-forensic-accountant-reveals-almost-70-of-alamedas-loans-were-serviced-with-ftx-customer-funds/'
informacionPost = obtenerContenidoPagina(url)

if informacionPost:
    
        print( "informacionPost",informacionPost)
else:
    print("No se pudo obtener información del post o el HTML del post-container.")
