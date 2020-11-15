from django.shortcuts import render
from django.utils import timezone
from .models import Card

def card_list(request): 
    cards = Card.objects.filter(published_date__lte=timezone.now()).order_by('published_date') 
    return render(request, 'bender/card_list.html', {'cards': cards})