import requests
from bs4 import BeautifulSoup

def obtener_enlaces_pagina(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            div_list_post = soup.find('div', class_='posts')

            if div_list_post:
                enlaces_list = []

                enlaces = div_list_post.find_all('a')

                for enlace in enlaces:
                    href = enlace.get('href')
                    if href:
                        enlaces_list.append(href)

                return enlaces_list  # Devuelve la lista de enlaces

            else:
                print("No se encontró el elemento <div class='posts'>")
                return []

        else:
            print(f"Error al hacer la solicitud. Código de respuesta: {response.status_code}")
            return []

    except Exception as e:
        print(f"Error al obtener la página: {e}")
        return []

# Ejemplo de uso
if __name__ == "__main__":
    url = 'https://cryptoslate.com/top-news/'
    enlaces = obtener_enlaces_pagina(url)
    
    if enlaces:
        print(enlaces)  
    else:
        print("No se encontraron enlaces.")
