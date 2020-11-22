from django.conf import settings
from django.db import models
from django.utils import timezone

class Card(models.Model):    
    titulo = models.CharField(max_length=500)
    fonte = models.CharField(max_length=500)
    data_criacao = models.DateTimeField(default=timezone.now)    
    texto = models.TextField()
    link = models.URLField(default="#")
    imagem = models.URLField(default="#")
    lido = models.BooleanField   

    def __str__(self):
        return self.titulo