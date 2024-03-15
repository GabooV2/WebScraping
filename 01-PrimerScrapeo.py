import requests

req = requests.get("https://example.com")

print(req.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(req.text)

print(soup.select("title")[0].getText())

# Seleccionar del segundo parágrafo el primer enlace 
a = soup.select("p")[1].select("a")[0]

# Mostrar su contenido
print(a.getText())

# Atributo con la dirección del enlace
a['href']

a.attrs.items() # Estos valores están mapeados del diccionario "attrs"

for meta in soup.select("meta"):
    for atributo, valor in meta.attrs.items():
        print(f"{atributo}: {valor}")