from datetime import datetime
from django.shortcuts import render
from django.utils import timezone
from .models import Card
from django.shortcuts import redirect
from bs4 import BeautifulSoup
import requests

def card_list(request): 
     # dia por extenso
    agora = datetime.now()    
    dia_extenso = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    mes_extenso = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", 
    "Dezembro"]
    dia = agora.weekday()
    mes = agora.month
    hoje = dia_extenso[dia] + ', ' + str(agora.day) + ' de ' + mes_extenso[mes - 1]
    hora = agora.hour
    saudacao = ", Mark"

    if hora >= 5 and hora <= 12:
       saudacao = "Bom dia" + saudacao
    elif hora > 12 and hora <= 17:
       saudacao = "Boa tarde" + saudacao
    else:
        saudacao = "Boa noite" + saudacao

    cards = Card.objects.filter(data_criacao__lte=timezone.now()).order_by('data_criacao')         
    return render(request, 'hoje/card_list.html', {'cards': cards, 'hoje': hoje, 'saudacao' : saudacao})

def card_update_mirante(request):
    card = Card()

    html = requests.get("https://imirante.com/").content
    soup = BeautifulSoup(html, 'html.parser')
    
    #link
    noticia = soup.find("a", class_="materiaDestaqueHorizontalCheia-link")
    card.link = noticia['href']

    txt = str(noticia)

    #imagem
    i = txt.index("(") + 2
    imagem = ''

    while i < len(txt):
        
        if txt[i] == "'":
            i = 1000
        else:
            imagem = imagem + txt[i]
        
        i += 1
    
    card.imagem = imagem

    #titulo
    txt = str(noticia)

    i = txt.index("alt=") + 5
    titulo = ''

    while i < len(txt):
        
        if txt[i] == "\"":
            i = 1000
        else:
            titulo = titulo + txt[i]
        
        i += 1

    card.titulo = titulo

    card.fonte = "Mirante"
    card.data_criacao = timezone.now()
    
    #salva somente nao salvou ainda
    if Card.objects.filter(titulo=titulo):
        print("Repetido")
    else:
        card.save()

    return redirect('card_list')


def card_update_versiculo(request):
    card = Card()
    
    html = requests.get("https://www.bible.com/pt/verse-of-the-day").content
    soup = BeautifulSoup(html, 'html.parser')
    
    titulo = 'Versículo do Dia'
    card.titulo = titulo
    card.fonte = soup.find("p", class_="usfm fw7 mt0 mb0 gray f7 ttu").get_text()
    card.data_criacao = timezone.now()
    card.texto = soup.find("p", class_="near-black mt0 mb2").get_text()
    card.link = 'https://www.bible.com/pt/verse-of-the-day'
    
    #imagem
    txt = soup.prettify()
    i = txt.index("imageproxy") + 5
    imagem = ''

    while i < len(txt):
        
        if txt[i] == "\"":
            i = 1000000
        else:
            imagem = imagem + txt[i]
        
        i += 1

    imagem = "//image" + imagem
    card.imagem = imagem
    
    #salva somente nao salvou ainda
    if Card.objects.filter(titulo=titulo):
        print("Repetido")
    else:
        card.save()

    return redirect('card_list')