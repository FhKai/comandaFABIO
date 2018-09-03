from django.shortcuts import render
from .models import Restaurante

def lista_de_restaurantes(request):
    restaurantes = Restaurante.objects.all().order_by('nome')
    return render(request, 'restaurante/restaurantes.html', {'restaurantes':restaurantes})
