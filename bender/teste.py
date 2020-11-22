from bs4 import BeautifulSoup
import requests
import cssutils

html = requests.get("https://www.bible.com/pt/verse-of-the-day").content

soup = BeautifulSoup(html, 'html.parser')

# print(soup.prettify())

temperatura = soup.find("p", class_="near-black mt0 mb2").get_text()

print(temperatura)

temperatura = soup.find("p", class_="usfm fw7 mt0 mb0 gray f7 ttu").get_text()

print(temperatura)

txt = soup.prettify()

#imagem
i = txt.index("imageproxy") + 5
imagem = ''

while i < len(txt):
    
    if txt[i] == "\"":
        i = 1000000
    else:
        imagem = imagem + txt[i]
    
    i += 1

print(imagem)