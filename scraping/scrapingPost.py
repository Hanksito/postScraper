import requests
from bs4 import BeautifulSoup

class PostContent:
    def __init__(self, title, subheading, image_url, paragraphs, h2_headings):
        self.title = title
        self.subheading = subheading
        self.image_url = image_url
        self.paragraphs = paragraphs
        self.h2_headings = h2_headings

    def __str__(self):
        return f"Title: {self.title}\nSubheading: {self.subheading}\nImage URL: {self.image_url}\nParagraphs: {self.paragraphs}\nH2 Headings: {self.h2_headings}"

def obtener_contenido_pagina(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            post_container = soup.find('div', class_='post-container')

            title = post_container.find('h1', class_='post-title')
            subheading = post_container.find('p', class_='post-subheading')
            image_url = post_container.find('img', class_='nolazy')['src']
            paragraphs = [p.get_text() for p in post_container.find_all('p', class_=None)]
            h2_headings = [h2.get_text() for h2 in post_container.find_all('h2')]

            content = PostContent(
                title.get_text() if title else "",
                subheading.get_text() if subheading else "",
                image_url if image_url else "",
                paragraphs,
                h2_headings
            )

            return content
        else:
            print(f"Error al hacer la solicitud. Código de respuesta: {response.status_code}")
    except Exception as e:
        print(f"Error al obtener la página: {e}")

if __name__ == "__main__":
    url = 'https://cryptoslate.com/sec-drops-charges-against-ripple-executives/'
    contenido = obtener_contenido_pagina(url)

    # Imprime el objeto PostContent en la consola
    print(contenido)
