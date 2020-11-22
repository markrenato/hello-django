from datetime import datetime
from django.shortcuts import render
from django.utils import timezone
from .models import Card

def card_list(request): 
    cards = Card.objects.filter(data_criacao__lte=timezone.now()).order_by('data_criacao')         
    return render(request, 'hoje/card_list.html', {'cards': cards})