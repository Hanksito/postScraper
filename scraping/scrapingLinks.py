import requests
from bs4 import BeautifulSoup

def obtenerEnlacesPagina(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            div24Hours = soup.find('section', {'id': '24Hours'})
            if div24Hours:
                divListPost = div24Hours.find('div', class_='posts')
                if divListPost:
                    enlacesList = []

                    enlaces = divListPost.find_all('a')

                    for enlace in enlaces:
                        href = enlace.get('href')
                        if href:
                            enlacesList.append(href)

                    return enlacesList  

                else:
                    print("No se encontró el elemento 'list-post'")
                    return []

            else:
                print("No se encontró la sección")
                return []

        else:
            print(f"Error al hacer la solicitud. Código de respuesta: {response.status_code}")
            return []

    except Exception as e:
        print(f"Error al obtener la página: {e}")
        return []

