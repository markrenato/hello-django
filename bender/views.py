from datetime import datetime
from django.shortcuts import render
from django.utils import timezone
from .models import Card

def card_list(request): 
    # dia por extenso
    agora = datetime.now()    
    dia_extenso = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]
    mes_extenso = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", 
    "Dezembro"]
    dia = agora.weekday()
    mes = agora.month
    hoje = dia_extenso[dia] + ',' + str(agora.day) + ' de ' + mes_extenso[mes - 1]

    cards = Card.objects.filter(published_date__lte=timezone.now()).order_by('published_date')         
    return render(request, 'bender/card_list.html', {'cards': cards, 'hoje': hoje})