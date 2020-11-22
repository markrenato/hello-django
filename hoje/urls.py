from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_list, name='card_list'),
    path('card/update/mirante', views.card_update_mirante, name='card_update_mirante'),
    path('card/update/versiculo', views.card_update_versiculo, name='card_update_versiculo'),
]