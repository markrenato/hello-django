from django.db import models
from models import Card
from bs4 import BeautifulSoup
import requests
import cssutils


html = requests.get("https://imirante.com/").content

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())

temperatura = soup.find("a", class_="materiaDestaqueHorizontalCheia-link")

#print(temperatura)

print("Link: " + temperatura['href'])
txt = str(temperatura)

#imagem
i = txt.index("(") + 2
imagem = ''

while i < len(txt):
    
    if txt[i] == "'":
        i = 1000
    else:
        imagem = imagem + txt[i]
    
    i += 1

print("Imagem: " + imagem)

#titulo
txt = str(temperatura)

i = txt.index("alt=") + 5
imagem = ''

while i < len(txt):
    
    if txt[i] == "\"":
        i = 1000
    else:
        imagem = imagem + txt[i]
    
    i += 1

print("Titulo: " + imagem)

